
from pathlib import Path

def word_extract(path:str,content:str):
    """该工具函数用于把提取的关键词写入对应文件"""
    """如果是搜索关键词，path参数写search_word.txt"""
    """如果是筛选关键词，path参数写screen_word.txt"""


    agent_dir=Path(__file__).parent.parent.parent.parent
    
    file_path=agent_dir/path

    with open(file_path,'w',encoding='utf-8') as f:
        f.write(content)