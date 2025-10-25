#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
改进的客服数据处理工具
保留完整的问题描述并添加根因分析
"""

import re
from typing import List, Dict

def sanitize_sensitive_data(text: str) -> str:
    """脱敏处理敏感数据"""
    if not text:
        return text
    
    # URL脱敏
    text = re.sub(r'(https?://[^\s]+)', lambda m: m.group(1).split('/')[0] + '/...[已脱敏]', text)
    
    # 密钥/token脱敏
    text = re.sub(r'([A-Za-z0-9]{20,})', '[密钥已脱敏]', text)
    
    # 邮箱脱敏
    text = re.sub(r'[\w\.-]+@[\w\.-]+', '[邮箱已脱敏]', text)
    
    # 电话号码脱敏
    text = re.sub(r'1[3-9]\d{9}', '[电话已脱敏]', text)
    
    # IP地址脱敏
    text = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '[IP已脱敏]', text)
    
    return text

def extract_customer_service_answer(dialogue: str) -> str:
    """从对话中提取客服的回答"""
    service_responses = []
    lines = dialogue.split('\n')
    
    for line in lines:
        if line.startswith('**客服**：'):
            response = line.replace('**客服**：', '').strip()
            if response and response not in service_responses:
                service_responses.append(response)
    
    return '\n'.join(service_responses)

def analyze_root_cause(title: str, description: str, dialogue: str, category: str) -> str:
    """分析问题根因"""
    dialogue_lower = dialogue.lower()
    desc_lower = (description + title).lower()
    
    # 配置类问题
    if any(keyword in desc_lower for keyword in ['配置', '设置', '域名', 'cdn', 'ssl']):
        if '测试未通过' in desc_lower or '未通过' in dialogue_lower:
            return "配置参数不正确或源站响应异常"
        if '审核' in desc_lower or '审核中' in dialogue_lower:
            return "证书或配置正在审核中，需等待系统处理"
        if '处理中' in desc_lower:
            return "系统配置下发延迟，需要手动介入处理"
        return "配置参数或流程设置不当"
    
    # 权限/认证问题
    if any(keyword in desc_lower for keyword in ['私有', '公开', 'token', '权限', '认证']):
        if '私有空间' in dialogue_lower or '私有' in desc_lower:
            return "存储空间权限设置为私有，导致公开访问受限"
        if 'token' in desc_lower and '过期' in desc_lower:
            return "使用了带token的URL访问公开空间，不需要token参数"
        if '实名认证' in desc_lower:
            return "可能存在重复实名认证账号或信息填写错误"
        return "访问权限或认证配置不正确"
    
    # 上传下载问题
    if any(keyword in desc_lower for keyword in ['上传', '下载', '访问', '显示']):
        if '612' in dialogue or '612' in description:
            return "文件不存在或上传时key参数指定不正确"
        if '测试域名' in dialogue_lower or 'bkt.clouddn.com' in desc_lower:
            return "使用了测试域名，应该绑定经过备案的CDN加速域名"
        if '国内' in desc_lower and '国外' in desc_lower:
            return "测试域名在国内访问受限，需要使用备案域名"
        return "文件访问路径错误或域名配置问题"
    
    # CDN/缓存问题
    if 'cdn' in category.lower() or '流量' in desc_lower or '缓存' in desc_lower:
        if '删除' in desc_lower and '流量' in desc_lower:
            return "CDN缓存未刷新，删除的文件仍可通过缓存访问"
        return "CDN缓存或配置问题"
    
    # SDK使用问题
    if 'sdk' in category.lower() or '接口' in desc_lower or 'api' in desc_lower.lower():
        return "SDK使用方法不正确或参数传递错误"
    
    # 默认分析
    return "需要根据具体错误信息和配置进一步排查"

def process_section(section: str, section_num: int) -> str:
    """处理单个章节，保留完整信息并添加根因分析"""
    
    # 提取标题
    title_match = re.search(r'^## (.+?)$', section, re.MULTILINE)
    if not title_match:
        return None
    title = title_match.group(1).strip()
    
    # 提取分类
    category_match = re.search(r'\*\*分类\*\*：(.+?)$', section, re.MULTILINE)
    category = category_match.group(1).strip() if category_match else "未分类"
    
    # 提取问题描述
    desc_match = re.search(r'### 问题描述\s*\n\n(.+?)(?=\n### 对话过程|\n---|\Z)', section, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else "无详细描述"
    
    # 提取对话过程
    dialogue_match = re.search(r'### 对话过程\s*\n\n(.+?)(?=\n---|\Z)', section, re.DOTALL)
    dialogue = dialogue_match.group(1).strip() if dialogue_match else ""
    
    # 提取客服答案
    answer = extract_customer_service_answer(dialogue)
    if not answer:
        answer = "客服正在处理中"
    
    # 分析根因
    root_cause = analyze_root_cause(title, description, dialogue, category)
    
    # 脱敏处理
    description_sanitized = sanitize_sensitive_data(description)
    answer_sanitized = sanitize_sensitive_data(answer)
    
    # 格式化输出
    result = f"""## Q{section_num}: {title}

**问题分类**: {category}

**问题描述**:
{description_sanitized}

**客服解答**:
{answer_sanitized}

**根本原因**:
{root_cause}

---
"""
    
    return result

def process_document(input_file: str, output_file: str, batch_start: int = 1, batch_size: int = 5):
    """处理文档的指定批次"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按 --- 分割章节
    sections = re.split(r'\n---\n', content)
    sections = [s.strip() for s in sections if s.strip() and s.strip().startswith('##')]
    
    # 计算批次范围
    batch_end = min(batch_start + batch_size - 1, len(sections))
    
    print(f"文档共 {len(sections)} 个章节")
    print(f"处理批次: {batch_start}-{batch_end}")
    
    # 处理指定批次
    results = []
    for i in range(batch_start - 1, batch_end):
        section = sections[i]
        processed = process_section(section, i + 1)
        if processed:
            results.append(processed)
            print(f"✓ 处理完成章节 {i + 1}")
    
    # 写入或追加到输出文件
    mode = 'a' if batch_start > 1 else 'w'
    with open(output_file, mode, encoding='utf-8') as f:
        if batch_start == 1:
            f.write("# 客服对话数据处理结果\n\n")
            f.write("> 本文档包含结构化的客服对话记录，已进行隐私脱敏处理\n\n")
        f.write('\n'.join(results))
    
    print(f"\n✓ 批次 {batch_start}-{batch_end} 处理完成")
    print(f"输出文件: {output_file}")
    
    return len(sections), batch_end

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("使用方法: python improved_data_processor.py <输入文件> <输出文件> [起始章节] [批次大小]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    batch_start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    batch_size = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    
    total, processed_end = process_document(input_file, output_file, batch_start, batch_size)
    
    if processed_end < total:
        print(f"\n还有 {total - processed_end} 个章节待处理")
        print(f"继续处理: python improved_data_processor.py {input_file} {output_file} {processed_end + 1} {batch_size}")
