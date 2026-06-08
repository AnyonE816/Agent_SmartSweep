'''     # 调用这个脚本，对config里的.yml各文件，进行load和编辑
yaml：配置文件处理器（工程）        平时：python代码，config.py
k: v
'''
import yaml
from utils.path_tool import get_abs_path


# RAG 配置文件
def load_rag_config(config_path: str=get_abs_path("config/rag.yml"), encoding="utf-8"):
    with open(config_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)    # FullLoader全量加载

# chroma向量数据库 ~
def load_chroma_config(config_path: str=get_abs_path("config/chroma.yml"), encoding="utf-8"):
    with open(config_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)    # FullLoader全量加载

# Prompts ~
def load_prompts_config(config_path: str=get_abs_path("config/prompts.yml"), encoding="utf-8"):
    with open(config_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)    # FullLoader全量加载

# Agent ~
def load_agent_config(config_path: str=get_abs_path("config/agent.yml"), encoding="utf-8"):
    with open(config_path, "r", encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)    # FullLoader全量加载


rag_config = load_rag_config()
chroma_config = load_chroma_config()
prompt_config = load_prompts_config()
agent_config = load_agent_config()


# 测试
if __name__ == '__main__':
    print(rag_config["chat_model_name"])
    print(rag_config["embedding_model_name"])