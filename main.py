import streamlit as st
import time
import asyncio

from utils import ben_robot, ben_robot_baidu  # 假设这个函数能正常返回回复
from langchain.memory import ConversationBufferMemory


# 打字机效果函数
def typewriter_effect(text, speed=0.05):
    # 创建一个空容器用于动态更新内容
    container = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        container.markdown(typed_text)  # 逐步更新显示内容
        time.sleep(speed)  # 控制打字速度
    return container


st.title("🐖笨笨-2.0")
st.info("2.1版本更新，增加了天气及世家查询模块")
# 初始化会话状态
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{
        "role": "ai",
        "content": "小宝宝，怎么啦？"}]

# 初始化模式选择状态 - 使用字符串而不是数字
if "mode" not in st.session_state:
    st.session_state["mode"] = "聊天模式"  # 默认模式

with st.sidebar:
    st.header("回答模式设置")

    # 使用单选按钮替代普通按钮，确保只能选择一个模式
    mode_option = st.radio(
        "选择回答模式:",
        ["聊天模式", "百科顿悟模式"],
        index=0 if st.session_state["mode"] == "聊天模式" else 1
    )

    # 更新模式状态
    st.session_state["mode"] = mode_option

    # 显示当前模式
    st.write(f"**当前模式:** {st.session_state['mode']}")

# 显示历史消息
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

# 处理用户输入
prompt = st.chat_input("说吧(deep seek-V3.1)")
if prompt:
    # 添加用户消息到会话历史并显示
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    num = 2
    # 获取AI回复
    with st.spinner("emmmmmm"):
        if st.session_state["mode"] == "聊天模式":
            response = ben_robot(prompt, st.session_state["memory"])
            print(response)

            while response == "":
                response = ben_robot(prompt, st.session_state["memory"])
                num+=1
                print(num)
        else:
            response = ben_robot_baidu(prompt, st.session_state["memory"])
            print(response)
            while response == "":
                response = ben_robot_baidu(prompt, st.session_state["memory"])

                num += 1
                print(num)



    # 添加AI回复到会话历史
    st.session_state["messages"].append({"role": "ai", "content": response})

    # 用打字机效果显示AI回复
    with st.chat_message("ai"):
        typewriter_effect(response, speed=0.03)  # 可调整speed控制打字速度（秒/字符）

