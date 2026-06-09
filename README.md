# SmartSweep智扫通-扫地机器人智能客服系统

基于 RAG + React Agent 架构的智能客服系统，专为扫地机器人产品打造，支持知识库问答、用户数据查询、个性化报告生成等功能。

<video width="800" controls>
  <source src="demo.mp4" type="video/mp4">
</video>

> 💡 若视频无法播放，可直接在项目根目录中查看 `demo.mp4` 原文件

## 项目介绍

这是一个智能客服系统的个人学习项目，采用了当前最流行的大模型应用架构：
- **RAG（检索增强生成）**：基于产品知识库实现精准的问答，解决大模型幻觉问题
- **React Agent**：智能体架构，支持多工具调用，能自动根据用户问题选择合适的工具
- **动态中间件**：支持动态提示词切换，实现不同场景下的不同处理逻辑
- **Streamlit WebUI**：开箱即用的网页交互界面，支持流式输出

## 核心功能

- ✅ **知识库问答**：基于产品手册、FAQ等文档，自动回答用户的产品问题
- ✅ **用户数据查询**：支持查询用户的设备使用记录、耗材状态、清洁效率等
- ✅ **个性化报告生成**：自动为用户生成月度/季度的使用报告和保养建议
- ✅ **天气查询**：支持查询用户所在城市的天气，辅助推荐清洁时机
- ✅ **流式输出**：支持打字机效果的流式回答，提升用户体验
- ✅ **完整日志**：全链路日志记录，方便问题排查
- ✅ **配置化管理**：所有参数统一配置，支持快速调整

## 技术栈

| 模块 | 技术 |
|:----:|:----:|
| **大模型** | 通义千问（Qwen）、DashScope Embedding |
| **Agent框架** | LangChain Agent、LangGraph |
| **RAG** | Chroma 向量数据库、LangChain RAG |
| **文档处理** | PyPDFLoader、TextLoader、RecursiveCharacterTextSplitter |
| **Web界面** | Streamlit |
| **配置管理** | YAML 配置文件 |
| **工程化** | 统一日志、路径管理、MD5去重 |

## 项目架构

```bash
SmartSweep/
├── agent/
│   ├── __init__.py
│   ├── react_agent.py
│   └── tools/
│       ├── __init__.py
│       ├── agent_tools.py
│       └── middleware.py
├── model/
│   ├── __init__.py
│   └── factory.py
├── rag/
│   ├── __init__.py
│   ├── rag_service.py
│   └── vector_store.py
├── utils/
│   ├── __init__.py
│   ├── config_handler.py
│   ├── file_handler.py
│   ├── logger_handler.py
│   ├── path_tool.py
│   └── prompt_loader.py
├── config/
├── prompt/
├── data/
├── app.py
├── requirements.txt
└── README.md
```

## 目录说明
| 目录/文件 | 功能说明 |
|----|----|
| `agent/` | 智能体核心模块，存放 Agent 工具、中间件与 React Agent 主逻辑 |
| `chroma_db/` | Chroma 向量数据库，存储嵌入后的知识库向量数据 |
| `config/` | 项目配置中心，存放所有 YAML 格式的配置文件 |
| `data/` | 本地知识库目录，存放扫地机器人相关的产品文档 |
| `logs/` | 运行日志目录，存储全链路操作日志 |
| `model/` | 模型工厂，统一管理大模型、嵌入模型的初始化与调用 |
| `prompt/` | 提示词模板目录，存放不同场景下的系统提示词与任务模板 |
| `rag/` | 检索增强生成（RAG）核心模块，实现文档加载、分片、检索与问答拼接 |
| `utils/` | 全局通用工具库，提供配置加载、文件处理、日志管理、路径工具等通用功能 |
| `app.py` | 项目入口主程序，Streamlit 网页交互界面的启动文件 |
| `README.md` | 项目说明文档，包含项目介绍、架构与快速开始指南等 |
| `requirements.txt` | 项目依赖清单，记录所需第三方库及版本 |


## 快速开始
```bash
# 1. 克隆项目
git clone https://github.com/yourname/SmartSweep.git
cd SmartSweep

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置通义千问API Key
export DASHSCOPE_API_KEY= # 运行请输入您自己的API哦✌️

# 4. 首次运行需先加载知识库到向量库
python rag/vector_store.py

# 4. 启动智能客服
streamlit run app.py
```

