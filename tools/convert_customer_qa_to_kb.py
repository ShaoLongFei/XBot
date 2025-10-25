#!/usr/bin/env python3
"""
客服问答数据转换工具 - 策略1：整合完整对话

将客服问答 JSON 数据转换为适合知识库导入的完整对话格式。
"""

import json
import re
from html import unescape
from pathlib import Path
import argparse


def clean_html(text: str) -> str:
    """
    移除 HTML 标签并清理文本
    
    Args:
        text: 包含 HTML 标签的原始文本
        
    Returns:
        清理后的纯文本
    """
    text = re.sub(r'<img[^>]+>', '[图片]', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    text = re.sub(r'\n\s*\n', '\n', text)
    return text.strip()


def convert_to_full_conversation(item: dict) -> str:
    """
    策略1：整合完整对话
    将单个工单转换为包含完整对话流程的知识条目
    
    Args:
        item: 单个客服工单数据
        
    Returns:
        格式化后的完整对话文本
    """
    content = f"标题：{item['title']}\n"
    content += f"分类：{item['category']}\n\n"
    
    if item.get('description'):
        desc = clean_html(item['description'])
        if desc:
            content += f"问题描述：\n{desc}\n\n"
    
    content += "对话过程：\n"
    for reply in item['replies']:
        role = "客户" if reply['owner'] == 'customer' else "客服"
        cleaned = clean_html(reply['content'])
        if cleaned:
            content += f"{role}：{cleaned}\n\n"
    
    return content.strip()


def process_json_file(input_path: str, output_path: str = None, output_format: str = 'txt'):
    """
    处理 JSON 文件并转换为知识库格式
    
    Args:
        input_path: 输入 JSON 文件路径
        output_path: 输出文件路径（可选）
        output_format: 输出格式 ('txt' 或 'json')
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"找不到输入文件: {input_path}")
    
    print(f"📖 读取文件: {input_path}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not isinstance(data, list):
        raise ValueError("JSON 文件必须是一个数组")
    
    print(f"📊 共找到 {len(data)} 条客服记录")
    
    converted_data = []
    for idx, item in enumerate(data, 1):
        try:
            converted_text = convert_to_full_conversation(item)
            converted_data.append({
                'id': item.get('id'),
                'title': item.get('title'),
                'category': item.get('category'),
                'content': converted_text
            })
            if idx % 100 == 0:
                print(f"✓ 已处理 {idx}/{len(data)} 条记录...")
        except Exception as e:
            print(f"✗ 处理工单 {item.get('id', 'unknown')} 失败: {e}")
            continue
    
    if not output_path:
        output_path = input_file.parent / f"{input_file.stem}_converted.{output_format}"
    
    output_file = Path(output_path)
    
    if output_format == 'txt':
        print(f"💾 保存为文本格式: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            for item in converted_data:
                f.write("=" * 80 + "\n")
                f.write(item['content'])
                f.write("\n" + "=" * 80 + "\n\n")
    
    elif output_format == 'json':
        print(f"💾 保存为 JSON 格式: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(converted_data, f, ensure_ascii=False, indent=2)
    
    else:
        raise ValueError(f"不支持的输出格式: {output_format}")
    
    print(f"\n✅ 转换完成！")
    print(f"   成功转换: {len(converted_data)}/{len(data)} 条记录")
    print(f"   输出文件: {output_file}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='客服问答数据转换工具 - 将 JSON 数据转换为知识库可导入的完整对话格式',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 基本使用（输出为 txt 格式）
  python convert_customer_qa_to_kb.py customer_qa.json
  
  # 指定输出文件和格式
  python convert_customer_qa_to_kb.py customer_qa.json -o output.json -f json
  
  # 输出为文本文件
  python convert_customer_qa_to_kb.py customer_qa.json -o converted.txt -f txt
        """
    )
    
    parser.add_argument('input', help='输入 JSON 文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')
    parser.add_argument('-f', '--format', 
                       choices=['txt', 'json'],
                       default='txt',
                       help='输出格式 (默认: txt)')
    
    args = parser.parse_args()
    
    try:
        process_json_file(args.input, args.output, args.format)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
