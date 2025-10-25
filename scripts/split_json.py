#!/usr/bin/env python3
import json
import sys
import os
from pathlib import Path


def split_json_array(input_file_path, num_splits=10):
    input_path = Path(input_file_path)
    
    if not input_path.exists():
        print(f"错误：文件 '{input_file_path}' 不存在")
        sys.exit(1)
    
    if not input_path.is_file():
        print(f"错误：'{input_file_path}' 不是一个文件")
        sys.exit(1)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"错误：无法解析 JSON 文件 - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误：读取文件失败 - {e}")
        sys.exit(1)
    
    if not isinstance(data, list):
        print("错误：JSON 文件内容不是数组")
        sys.exit(1)
    
    total_items = len(data)
    if total_items == 0:
        print("警告：JSON 数组为空")
        return
    
    items_per_split = (total_items + num_splits - 1) // num_splits
    
    output_dir = input_path.parent
    base_name = input_path.stem
    extension = input_path.suffix
    
    print(f"开始切分文件：{input_file_path}")
    print(f"总计 {total_items} 个元素，将切分为 {num_splits} 个文件")
    print(f"每个文件约 {items_per_split} 个元素")
    print()
    
    for i in range(num_splits):
        start_idx = i * items_per_split
        end_idx = min((i + 1) * items_per_split, total_items)
        
        if start_idx >= total_items:
            break
        
        split_data = data[start_idx:end_idx]
        
        output_file = output_dir / f"{base_name}_part_{i+1:02d}{extension}"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(split_data, f, ensure_ascii=False, indent=2)
            print(f"✓ 已创建：{output_file.name} ({len(split_data)} 个元素)")
        except Exception as e:
            print(f"✗ 创建文件失败：{output_file.name} - {e}")
            sys.exit(1)
    
    print()
    print("切分完成！")


def main():
    if len(sys.argv) < 2:
        print("用法: python split_json.py <json文件路径> [切分数量]")
        print("示例: python split_json.py data.json 10")
        print()
        print("参数说明:")
        print("  <json文件路径>  - 要切分的 JSON 文件路径（必需）")
        print("  [切分数量]      - 切分的文件数量（可选，默认为 10）")
        sys.exit(1)
    
    input_file = sys.argv[1]
    num_splits = 10
    
    if len(sys.argv) >= 3:
        try:
            num_splits = int(sys.argv[2])
            if num_splits <= 0:
                print("错误：切分数量必须大于 0")
                sys.exit(1)
        except ValueError:
            print("错误：切分数量必须是一个整数")
            sys.exit(1)
    
    split_json_array(input_file, num_splits)


if __name__ == "__main__":
    main()
