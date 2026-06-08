
""" 增强 Prompt
rag总结服务：（用户提问+参考资料 = 增强版prompt）  --->  交给模型

一整套逻辑：用户输入prompt +   转成向量1321 ->    进入chroma + 对比与内部资料各向量的相似度 + 提取出向量最相似的k个资料段 -> 组合成增强prompt -> 喂给大模型回答
               ⬆                ⬆               ⬆                ⬆                         ⬆                     ⬆                ⬆
           p_t{input}    retriever(用embed)   retriever        向量相似度对比                retriever         p_t里拼接一下 用p+资p     chain
"""
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model

def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
    return prompt

# str_parser = StrOutputParser()

class RagSummarizeService(object):
    def __init__(self):
        self.vector_store = VectorStoreService()
        self.retriever = self.vector_store.get_retriever()
# 详解retriever: 进、取、吐（进：将用户prompt转为向量embedding；取：对比chroma中各资料的向量；吐：给出最相似的k个资料）
        self.prompt_text = load_rag_prompts()
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)
        self.model = chat_model
        self.chain = self._init_chain()

    def _init_chain(self):  # 构建链，返回链：工程中定义放在函数类中，不单个存在
        chain = self.prompt_template | print_prompt | self.model | StrOutputParser()    # 调用类不加括号，直接调用函数加括号
        return chain

    def retriever_docs(self, query: str) -> list[Document]:     # 取合适参考资料
        return self.retriever.invoke(query)

    def rag_summarize(self, query: str) -> str:

        content_docs = self.retriever_docs(query)

        context = ""
        counter = 0
        for doc in content_docs:
            counter += 1
            context += f"【参考资料{counter}】：参考资料：{doc.page_content} | 参考元数据：{doc.metadata}\n"

        return self.chain.invoke(
            {
                "input": query,
                "context": context,
            }
        )


if __name__ == '__main__':
    rag = RagSummarizeService()

    print(rag.rag_summarize("小户型适合哪些扫地机器人"))  # 输出(调用rag流程)。   当前仅基于参考资料的回答