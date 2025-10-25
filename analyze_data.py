#!/usr/bin/env python3
import os
import re
import glob

def extract_qa_sections(content):
    """Extract question and answer sections from markdown content"""
    sections = []
    
    # First try to extract using the pattern with standalone # (process_data_3.md style)
    # Pattern: ## title ... #\n## 详细问题描述 ... #\n## 客服解答内容 ... ---
    qa_blocks = re.findall(
        r'##\s+[^\n]+\s+\*\*问题分类\*\*[^\n]+\s+#\s*\n## 详细问题描述\s+(.*?)#\s*\n## 客服解答内容\s+(.*?)#\s*\n## 根本原因分析',
        content,
        re.DOTALL
    )
    for q, a in qa_blocks:
        sections.append({'question': q.strip(), 'answer': a.strip()})
    
    # If we found results, return (this file uses only one format)
    if sections:
        return sections
    
    # Otherwise try other patterns by splitting by ## sections
    questions = re.split(r'\n##\s+', content)
    
    for question_block in questions:
        if not question_block.strip():
            continue
        
        q_match = None
        a_match = None
        
        # Pattern 1: ### 详细问题描述 ... ### 客服解答
        q_match = re.search(r'### 详细问题描述\s+(.*?)(?=###|#\s*\n##)', question_block, re.DOTALL)
        a_match = re.search(r'### 客服解答\s+(.*?)(?=###|#\s*\n##|---|\Z)', question_block, re.DOTALL)
        
        # Pattern 2: ### 详细问题描述 ... ### 客服解答内容
        if not (q_match and a_match):
            q_match = re.search(r'### 详细问题描述\s+(.*?)(?=###|#\s*\n##)', question_block, re.DOTALL)
            a_match = re.search(r'### 客服解答内容\s+(.*?)(?=###|#\s*\n##|---|\Z)', question_block, re.DOTALL)
        
        # Pattern 2b: ### 详细问题描述 ... ### 客服解答过程
        if not (q_match and a_match):
            q_match = re.search(r'### 详细问题描述\s+(.*?)(?=###|#\s*\n##)', question_block, re.DOTALL)
            a_match = re.search(r'### 客服解答过程\s+(.*?)(?=###|#\s*\n##|---|\Z)', question_block, re.DOTALL)
        
        # Pattern 3: ### 问题描述 ... ### 客服解答
        if not (q_match and a_match):
            q_match = re.search(r'### 问题描述\s+(.*?)(?=###|#\s*\n##)', question_block, re.DOTALL)
            a_match = re.search(r'### 客服解答\s+(.*?)(?=###|#\s*\n##|---|\Z)', question_block, re.DOTALL)
        
        # Pattern 4: **问题描述**: ... **客服解答**: (support both : and ：)
        if not (q_match and a_match):
            q_match = re.search(r'\*\*问题描述\*\*[：:]\s+(.*?)(?=\*\*客服解答\*\*)', question_block, re.DOTALL)
            a_match = re.search(r'\*\*客服解答\*\*[：:]\s+(.*?)(?=\*\*根本原因|\*\*解决方案\*\*:|---|\Z)', question_block, re.DOTALL)
        
        if q_match and a_match:
            sections.append({
                'question': q_match.group(1).strip(),
                'answer': a_match.group(1).strip()
            })
    
    return sections

def calculate_avg_length(sections):
    """Calculate average character count for questions and answers"""
    if not sections:
        return 0
    
    total_chars = 0
    for section in sections:
        total_chars += len(section['question']) + len(section['answer'])
    
    return total_chars / len(sections)

def main():
    data_files = glob.glob('data/process_data_*.md')
    file_stats = []
    
    for file_path in data_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        sections = extract_qa_sections(content)
        avg_length = calculate_avg_length(sections)
        
        file_stats.append({
            'file': os.path.basename(file_path),
            'num_sections': len(sections),
            'avg_length': avg_length
        })
    
    # Sort by average length
    file_stats.sort(key=lambda x: x['avg_length'])
    
    # Calculate percentiles manually
    lengths = sorted([stat['avg_length'] for stat in file_stats])
    n = len(lengths)
    
    def percentile(data, p):
        k = (n - 1) * p / 100
        f = int(k)
        c = k - f
        if f + 1 < n:
            return data[f] + c * (data[f + 1] - data[f])
        else:
            return data[f]
    
    percentile_15 = percentile(lengths, 15)
    percentile_50 = percentile(lengths, 50)
    percentile_85 = percentile(lengths, 85)
    
    # Print results
    print("=" * 80)
    print("数据文件分析结果")
    print("=" * 80)
    print()
    
    print(f"总共分析文件数: {len(file_stats)}")
    print()
    
    print("各文件平均字数统计 (从低到高排列):")
    print("-" * 80)
    print(f"{'文件名':<25} {'问答对数':>10} {'平均字数':>15}")
    print("-" * 80)
    
    for stat in file_stats:
        print(f"{stat['file']:<25} {stat['num_sections']:>10} {stat['avg_length']:>15.1f}")
    
    print("-" * 80)
    print()
    
    print("分位数统计:")
    print(f"  15% 分位: {percentile_15:.1f} 字")
    print(f"  50% 分位 (中位数): {percentile_50:.1f} 字")
    print(f"  85% 分位: {percentile_85:.1f} 字")
    print()
    
    print("=" * 80)

if __name__ == "__main__":
    main()
