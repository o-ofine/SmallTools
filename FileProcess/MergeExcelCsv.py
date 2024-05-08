# _*_ coding:utf-8 _*_
# @Time:2024/4/29 16:32
# @Author:cui泡泡
# @File:合并excel和csv.py
# @Software:PyCharm
import os
import time
import sys
import pandas as pd
from FileProcess.LoggingRecord import log_and_error_handler


@log_and_error_handler
def merge_files(input_folder, output_folder):
    print("*"*20 + "合并开始" + "*"*20)
    start_time = time.time()    # 记录开始时间

    merged_df = pd.DataFrame()  # 创建一个空的 DataFrame 来存储合并后的数据

    print("开始读取需要合并的文件。。。")
    # 遍历输入文件夹中的所有文件
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # 检查文件扩展名，只处理 Excel 和 CSV 文件
            if file.endswith('.xlsx') or file.endswith('.xls') or file.endswith('.csv'):
                # 加载文件到 DataFrame
                file_df = pd.read_excel(os.path.join(root, file), sheet_name=0) if file.endswith(
                    '.xlsx') or file.endswith('.xls') else pd.read_csv(os.path.join(root, file))

                # 将文件 DataFrame 合并到已有的 DataFrame 中
                if merged_df.empty:
                    merged_df = file_df
                else:
                    start_time = time.time()
                    merged_df = pd.concat([merged_df, file_df], axis=0, ignore_index=True)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    # 输出进度信息
                    sys.stdout.write(f"\rMerged {len(merged_df)} rows in {elapsed_time:.2f} seconds\n")
                    sys.stdout.flush()
    print("文件全部读取完成。。。")
    print("汇总文件开始写入。。。")
    # 将合并后的 DataFrame 写入到输出文件夹中
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    try:
        merged_df.to_excel(os.path.join(output_folder, 'merged_data.xlsx'), index=False)
    except Exception as e:
        print(f"Error: {e}")
    print("汇总文件写入完成。。。")

    end_time = time.time()  # 记录结束时间
    run_time = end_time - start_time  # 计算运行时间
    print(f"Program_use_time: {run_time:.2f} seconds")  # 打印运行时间
    print("*" * 20 + "合并结束" + "*" * 20)

if __name__ == "__main__":  # 使用示例
    input_folder = r'C:\Users\Administrator\Desktop\new_file\output'
    output_folder = r'C:\Users\Administrator\Desktop\new_file\output'
    # input_folder = input("请提供需要合并文件夹的地址：")
    # output_folder = input("请提供合并文件输出的地址：")
    merge_files(input_folder, output_folder)
