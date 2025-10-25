#!/usr/bin/env python3
import re
import sys

def extract_main_question(title, description, conversation):
    title_clean = title.strip().replace('？', '?').replace('，', ',')
    if '?' in title_clean or '？' in title:
        return title
    return title + '?'

def extract_answer_and_solution(conversation, description):
    lines = conversation.strip().split('\n')
    
    customer_messages = []
    service_responses = []
    
    for line in lines:
        line = line.strip()
        if line.startswith('**客户**：'):
            content = line.replace('**客户**：', '').strip()
            content = re.sub(r'\[图片\]', '', content).strip()
            if content:
                customer_messages.append(content)
        elif line.startswith('**客服**：'):
            content = line.replace('**客服**：', '').strip()
            if content:
                service_responses.append(content)
    
    if not service_responses:
        return None, [], None
    
    core_answer = None
    solution_steps = []
    notes = []
    
    for resp in service_responses:
        resp_clean = resp
        if resp_clean.startswith('您好'):
            resp_clean = re.sub(r'^您好[，,、]*', '', resp_clean).strip()
        
        if any(keyword in resp for keyword in ['先', '建议', '需要', '可以参考', '绑定', '删除', '重新创建', '检查', '访问', '关闭']):
            solution_steps.append(resp_clean if resp_clean else resp)
        elif any(keyword in resp for keyword in ['注意', '测试域名', '不要使用', '必须']):
            notes.append(resp_clean if resp_clean else resp)
    
    if solution_steps:
        core_answer = "根据问题原因，需要按以下步骤处理："
    elif service_responses:
        first_resp = service_responses[0]
        if first_resp.startswith('您好'):
            first_resp = re.sub(r'^您好[，,、]*', '', first_resp).strip()
        core_answer = first_resp if first_resp else service_responses[0]
    
    return core_answer, solution_steps, notes

def extract_scenario(category, description):
    scenarios = []
    if '对象存储' in category:
        scenarios.append('对象存储')
    if 'CDN' in category:
        scenarios.append('CDN')
    if 'SSL' in description or 'ssl' in description.lower() or '证书' in description:
        scenarios.append('SSL证书')
    if '域名' in description:
        scenarios.append('域名配置')
    if '实名' in description:
        scenarios.append('实名认证')
    
    return '、'.join(scenarios) if scenarios else category.split('｜')[0]

def sanitize_privacy_data(text):
    text = re.sub(r'http://[a-zA-Z0-9\-\.]+\.cn[^\s]*', 'http://example.com/...[已脱敏]', text)
    text = re.sub(r'https://[a-zA-Z0-9\-\.]+\.cn[^\s]*', 'https://example.com/...[已脱敏]', text)
    
    text = re.sub(r'[A-F0-9]{64}', '[验证码已脱敏]', text)
    text = re.sub(r'[A-F0-9]{32}', '[密钥已脱敏]', text)
    
    return text

def process_section(section_text):
    lines = section_text.strip().split('\n')
    
    if not lines or not lines[0].startswith('## '):
        return None
    
    title = lines[0].replace('## ', '').strip()
    
    category = ''
    description = ''
    conversation = ''
    
    current_section = None
    conversation_lines = []
    
    for i, line in enumerate(lines[1:], 1):
        line = line.strip()
        
        if line.startswith('**分类**'):
            category = line.replace('**分类**：', '').strip()
        elif line.startswith('### 问题描述'):
            current_section = 'description'
        elif line.startswith('### 对话过程'):
            current_section = 'conversation'
        elif current_section == 'description' and line and not line.startswith('#'):
            description += line + ' '
        elif current_section == 'conversation' and line and not line.startswith('#'):
            conversation_lines.append(line)
    
    conversation = '\n'.join(conversation_lines)
    description = description.strip()
    
    question = extract_main_question(title, description, conversation)
    answer, solution_steps, notes = extract_answer_and_solution(conversation, description)
    scenario = extract_scenario(category, description + ' ' + conversation)
    
    if not answer:
        return None
    
    result = f"## Q: {question}\n\n"
    result += f"**A:** {answer}\n\n"
    
    if solution_steps:
        result += "**解决步骤**：\n"
        for i, step in enumerate(solution_steps[:5], 1):
            result += f"{i}. {step}\n"
        result += "\n"
    
    if notes:
        result += "**注意事项**：\n"
        for note in notes[:3]:
            result += f"- {note}\n"
        result += "\n"
    
    result += f"**适用场景**：{scenario}\n\n"
    result += "---\n"
    
    return sanitize_privacy_data(result)

def main():
    input_file = '/workspace/data/temp/source_data.md'
    output_file = '/workspace/processed_customer_service_data/processed_data.md'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = content.split('\n---\n')
    
    batch_size = 5
    start_idx = 0
    
    if len(sys.argv) > 1:
        start_idx = int(sys.argv[1])
    
    end_idx = min(start_idx + batch_size, len(sections))
    
    processed_sections = []
    for i in range(start_idx, end_idx):
        if i >= len(sections):
            break
        
        section = sections[i].strip()
        if not section:
            continue
        
        processed = process_section(section)
        if processed:
            processed_sections.append(processed)
            print(f"Processed section {i+1}/{len(sections)}")
    
    mode = 'a' if start_idx > 0 else 'w'
    with open(output_file, mode, encoding='utf-8') as f:
        f.write('\n'.join(processed_sections))
    
    print(f"\nProcessed sections {start_idx+1} to {end_idx}")
    print(f"Total sections: {len(sections)}")
    print(f"Remaining: {len(sections) - end_idx}")

if __name__ == '__main__':
    main()
