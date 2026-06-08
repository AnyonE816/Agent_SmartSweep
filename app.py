import streamlit as st
import time
from agent.react_agent import ReactAgent

# 标题
st.title("智扫通扫地机器人智能客服")
# 分割线
st.divider()

# session_state（长期保存，逃避st重复循环，避免重复）
if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()    # 类示例保存session_state中

if "message" not in st.session_state:
    st.session_state["message"] = []

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])  # 提取key值。每次问答把所有历史消息都打印一遍


# 用户输入提示词
prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    response_messages = []
    with st.spinner("智能客服思考中🤔..."):
        res_stream = st.session_state["agent"].execute_stream(prompt)    # 填入query即可用

        def capture(generator, cache_list):     # 把chunk从生成器里拿出并存入，别的什么也不干。
            for chunk in generator:             # 只为流式输出同时，让AI消息也保存
                cache_list.append(chunk)

                for char in chunk:              # 再套char一字符一字符返回，代替直接chunk一段一段返回
                    time.sleep(0.01)
                    yield char

        st.chat_message("assistant").write_stream(capture(res_stream, response_messages))
        st.session_state["message"].append({"role": "ai", "content": response_messages[-1]})    # 流式输出时，思考全过程显示，思考完后折叠 -> 只显示最后一条“回答”
        st.rerun()      # 刷新界面，仅保存“回答”（刷新掉思考过程，后续可改为“折叠思考过程”，但该过程中包含了工具