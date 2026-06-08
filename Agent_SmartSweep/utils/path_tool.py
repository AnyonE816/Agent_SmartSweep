''' 工具函数1/5
路径工具：为整个工程提供统一的绝对路径
'''
import os


def get_project_root():
    '''
    获取工程所在的 根目录
    :return: 字符串根目录
    '''
    # 当前文件的绝对路径1
    current_file = os.path.abspath(__file__)
    # 获取工程的根目录2，先获取文件所在文件夹绝对路径3
    current_dir = os.path.dirname(current_file)
    # 获取工程根目录3
    project_root = os.path.dirname(current_dir)

    return project_root


def get_abs_path(relative_path: str) -> str:
    '''
    给相对路径，返回绝对路径
    :param relative_path: 相对路径（文件名）
    :return: 绝对路径（工程根目录[当前所在] + 文件名 = 绝对路径）
                       ⬆调用上面函数
    '''
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)

if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))
