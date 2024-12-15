import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from utils import MEMORY
from agent import load_agent

st.set_page_config(page_title="Scientific Research Assistant", page_icon=":robot:")

st.header("Scientific Research Assistant")

strategy = st.radio(
    "Reasoning Strategy",
    ("plan_and_solve"),
)

tool_names = st.multiselect(
    "Select tools to assist your research:",
    [
        "arxiv",
        "wikipedia",
        "ddg_search",
    ],
    ["arxiv", "wikipedia", "ddg_search"]
)

if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()

avatars = {
    "human": "user",
    "ai": "assistant"
}
for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

agent_chain = load_agent(tool_names=tool_names, strategy=strategy)

if prompt := st.chat_input(placeholder="Enter your research query here..."):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.invoke(
            {"input": prompt},
            {"callbacks": [st_callback]}
        )
        st.write(response["output"])
