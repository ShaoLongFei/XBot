#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def split_json_array(input_file_path, num_splits=10):
    """
    将包含 JSON 数组的文件切分成多个小文件
    
    Args:
        input_file_path: 输入 JSON 文件路径
        num_splits: 切分数量,默认 10
    """
    input_path = Path(input_file_path)
    
    if not input_path.exists():
        print(f"错误: 文件 '{input_file_path}' 不存在")
        return
    
    print(f"正在读取文件: {input_file_path}")
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return
    except Exception as e:
        print(f"错误: 读取文件失败 - {e}")
        return
    
    if not isinstance(data, list):
        print("错误: JSON 文件根元素必须是数组")
        return
    
    total_items = len(data)
    print(f"数组总长度: {total_items}")
    
    if total_items == 0:
        print("警告: JSON 数组为空")
        return
    
    items_per_file = total_items // num_splits
    remainder = total_items % num_splits
    
    parent_dir = input_path.parent
    file_stem = input_path.stem
    file_suffix = input_path.suffix
    
    start_idx = 0
    for i in range(num_splits):
        current_size = items_per_file + (1 if i < remainder else 0)
        end_idx = start_idx + current_size
        
        chunk = data[start_idx:end_idx]
        
        output_filename = f"{file_stem}_part{i+1:02d}{file_suffix}"
        output_path = parent_dir / output_filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)
        
        print(f"已保存: {output_filename} (包含 {len(chunk)} 个元素)")
        
        start_idx = end_idx
    
    print(f"\n✅ 切分完成! 共生成 {num_splits} 个文件")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python split_json.py <json文件路径> [切分数量]")
        print("示例: python split_json.py data.json")
        print("示例: python split_json.py data.json 5")
        sys.exit(1)
    
    input_file = sys.argv[1]
    num_splits = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    split_json_array(input_file, num_splits)
