import streamlit as st
import time
from utils import ben_robot  # 假设这个函数能正常返回回复

# 页面标题
st.title("欢迎来到笨笨世界")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []
if "show_initial" not in st.session_state:
    st.session_state.show_initial = True
if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # 用于存储用户输入的临时变量

# 显示初始消息（只显示一次）
if st.session_state.show_initial:
    initial_text = "你来啦！小宝宝"
    placeholder = st.empty()
    for i in range(len(initial_text) + 1):
        placeholder.markdown(f"**{initial_text[:i]}**")
        time.sleep(0.1)
    st.session_state.messages.append({"role": "assistant", "content": initial_text})
    st.session_state.show_initial = False

# 显示历史对话
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f"**笨笨猪：{message['content']}**")
    else:
        st.markdown(f"小宝宝：{message['content']}")

# 如果对话未结束，显示输入框
if not st.session_state.conversation_ended:
    # 使用表单来更好地处理输入
    with st.form(key="user_input_form", clear_on_submit=True):  # 添加 clear_on_submit=True
        user_input = st.text_input(
            "小宝宝：",
            value=st.session_state.user_input,  # 使用 session_state 中的值
            key="user_input_widget"  # 使用不同的 key
        )
        submit_button = st.form_submit_button("发送")

    if submit_button:
        # 清空输入框
        st.session_state.user_input = ""

        # 添加用户消息到历史
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 检查是否结束对话
        if "再见" in user_input:
            st.session_state.conversation_ended = True
            goodbye_text = "笨笨猪：再见小宝宝，下次再来玩哦！"
            st.markdown(f"**{goodbye_text}**")
            st.session_state.messages.append({"role": "assistant", "content": goodbye_text})
            st.success("对话已结束，刷新页面可以重新开始")
        else:
            # 显示加载状态并获取回复
            with st.spinner("猪脑发烧中"):
                resp = ben_robot(user_input)

            # 用打字效果显示回复
            placeholder = st.empty()
            display_text = f"笨笨猪：{resp}"
            for i in range(len(display_text) + 1):
                placeholder.markdown(f"**{display_text[:i]}**")
                time.sleep(0.1)

            # 添加机器人回复到历史
            st.session_state.messages.append({"role": "assistant", "content": resp})

            # 使用rerun刷新界面
            st.rerun()
else:

    st.info("对话已结束，刷新页面可以重新开始")

