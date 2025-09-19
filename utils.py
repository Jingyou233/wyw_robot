from langchain.chains.conversation.base import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

def ben_robot(content):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             "你的名字叫‘郜志远’，外号是‘笨笨猪’也是你对自己的称呼，你在回复用户时要把‘我’换成‘笨笨猪’，你是专门为‘王雅雯’而打造的聊天机器人,你和她是主仆关系，她问你是谁的时候，你应该回答你们之间的关系，比如‘我是你的笨笨猪’，和你对话的有且只有这一个用户，你必须记得王雅雯是谁，无论用户给你回复什么信息，你都要在回复她以‘👋，小宝宝’作为称呼，随后再进行正常交流。如果她和你说‘早安’，你需要回复‘吾皇万岁万岁万万岁’，如果她说‘晚安’你要回复‘左边木马，右边木马，上巴木马，鼻巴木马，嘴巴木马，下巴略略’。"),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ]
    )
    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key="sk-oO4rncrorPMb4oCHIYRRYH0KLCb9fk3wFtGACVumCO50LK63",
        base_url="https://api.aigc369.com/v1")
    memory=ConversationBufferMemory(return_messages=True)
    chain=ConversationChain(llm=model,memory=memory,prompt=prompt)

    answer = chain.invoke(content)
    return answer["response"]