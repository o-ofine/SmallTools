# _*_ coding:utf-8 _*_
# @Time:2024/4/29 17:46
# @Author:cui泡泡
# @File:解压后合并文件.py
# @Software:PyCharm
from FileProcess.ExtractFiles import batch_extract_files
from FileProcess.MergeExcelCsv import merge_files

folder_path = r'C:\Users\Administrator\Desktop\new_file\input'
output_folder = r'C:\Users\Administrator\Desktop\new_file\output'

batch_extract_files(folder_path, output_folder)
merge_files(output_folder, output_folder)