import os, hashlib
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def get_file_md5_hex(file_path: str):    # 获取文件的md5的十六进制字符串（读文件往知识库里面加）

    if not os.path.exists(file_path):
        # print()       工程里一般不用print了，用应对各种情况的logger
        logger.error(f"[md5计算]文件{file_path}不存在")
        return

    if not os.path.isfile(file_path):
        logger.error(f"[md5计算]文件{file_path}不是文件")
        return

    md5_obj = hashlib.md5()

    # 避免文件过大，流式传入文件
    chunk_size = 4096   # 4kb分片，防止内存爆炸
    try:
        with open(file_path, "rb") as f:     # 以分片模式，计算文件md5：必须二进制读取
            while chunk := f.read(chunk_size): md5_obj.update(chunk)    # :=
        '''
        上面这一行（新版 := ） = 老版
        chunk = f.read(chunk_size)
        while chunk:
            md5_obj.update(chunk)
            chunk = f.read(chunk_size)
        '''
        md5_hex = md5_obj.hexdigest()
        return md5_hex
    except Exception as e:
        logger.error(f"计算文件{file_path}的md5失败：{str(e)}")
        return None


def listdir_with_allowed_type(path: str, allowed_types: tuple[str]):    # 返回文件夹内的文件列表（仅想要的文件格式）
    files = []

    if not os.path.isdir(path):     # 不是文件夹
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
        return allowed_types

    for f in os.listdir(path):      # 是文件夹：  os.listdir列出整个文件夹内部的东西
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))

    return tuple(files)     # 元组不可修改

def pdf_loader(file_path: str, passwd=None) -> list[Document]:
    return PyPDFLoader(file_path, passwd).load()

def txt_loader(file_path: str) -> list[Document]:       # Document——langchain特有，内部流通最方便！；Json是所有语言/系统的普通话
    return TextLoader(file_path, encoding='utf-8').load()