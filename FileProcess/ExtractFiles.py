# _*_ coding:utf-8 _*_
# @Time:2024/4/29 15:36
# @Author:cui泡泡
# @File:检索指定类型的文件路径.py
# @Software:PyCharm
import os
import time
import zipfile
import tarfile
import gzip
import bz2
from FileProcess.LoggingRecord import log_and_error_handler


@log_and_error_handler
def batch_extract_files(folder_path, output_folder):
    print("*" * 20 + "开始解压" + "*" * 20)
    start_time = time.time()  # 记录开始时间

    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    # 获取文件夹中所有的文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            # 仅处理压缩文件
            if file.endswith('.zip') or file.endswith('.tar') or file.endswith('.gz') or file.endswith('.bz2'):
                # 定义解压函数，根据文件扩展名使用不同的解压工具
                if file.endswith('.zip'):
                    def extract_zip(file_path, out_folder):
                        with zipfile.ZipFile(file_path, 'r') as zip:
                            zip.extractall(out_folder)
                    extract_zip(os.path.join(root, file), output_folder)
                elif file.endswith('.tar'):
                    def extract_tar(file_path, out_folder):
                        with tarfile.open(file_path, 'r') as tar:
                            tar.extractall(out_folder)
                    extract_tar(os.path.join(root, file), output_folder)
                elif file.endswith('.gz'):
                    def extract_gzip(file_path, out_folder):
                        with gzip.open(file_path, 'rb') as gzip_file:
                            with open(os.path.join(out_folder, os.path.splitext(file)[0] + '.txt'), 'wb') as out_file:
                                out_file.write(gzip_file.read())
                    extract_gzip(os.path.join(root, file), output_folder)
                elif file.endswith('.bz2'):
                    def extract_bz2(file_path, out_folder):
                        with bz2.open(file_path, 'rb') as bz2_file:
                            with open(os.path.join(out_folder, os.path.splitext(file)[0] + '.txt'), 'wb') as out_file:
                                out_file.write(bz2_file.read())
                    extract_bz2(os.path.join(root, file), output_folder)
                else:
                    print(f"Unsupported file format: {file}")

    end_time = time.time()  # 记录结束时间
    run_time = end_time - start_time  # 计算运行时间
    print(f"Program_use_time: {run_time:.2f} seconds")  # 打印运行时间
    print("*" * 20 + "解压完成" + "*" * 20)

if __name__ == '__main__':
    folder_path = r'C:\Users\Administrator\Desktop\new_file\input'
    output_folder = r'C:\Users\Administrator\Desktop\new_file\output'
    batch_extract_files(folder_path, output_folder)
