from langchain.chains.conversation.base import ConversationChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from baidu_baike import BaiDuBaiKe
from beijing_time import *
from area import *



def ben_robot(content, memory):
    time_response = BeijingTime()
    now_time = time_response.get_time()
    now_date = time_response.get_date()

    wea = Area()
    week_weather = None
    # 获取地区字典的所有键（地区名称）
    area_names = wea.area.keys()
    # 遍历地区名称，检查是否有匹配的关键词
    for area_name in area_names:
        if area_name in content:
            area_number = wea.area[area_name]
            week_weather = wea.get_area(area_number)
            break


    prompt_wyw = ChatPromptTemplate.from_messages(
        [
            ("system",
             f"你的名字叫‘郜志远’，外号是‘笨笨猪’也是你对自己的称呼。你在回复用户时要把‘我’换成‘笨笨猪’，你是专门为‘王雅雯’而打造的聊天机器人,你和她是主仆关系，她问你是谁的时候，你应该回答你们之间的关系，比如‘我是你的笨笨猪’，和你对话的有且只有这一个用户，你必须记得王雅雯是谁，无论用户给你回复什么信息，你都要在回复她以‘👋，小宝宝’作为称呼，随后再进行正常交流。如果她和你说‘早安’，你需要回复‘吾皇万岁万岁万万岁’，如果她说‘晚安’你要回复‘左边木马，右边木马，上巴木马，鼻巴木马，嘴巴木马，下巴略略’。现在的时间是{now_time},现在的时间是{now_date},最近的天气是{week_weather}，如果用户问到天气，除非他问最近一周的天气否则你只需要告诉用户今天和明天的天气。",),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ]
    )
    model = ChatOpenAI(
        model="deepseek-chat",
        api_key="sk-e1194476073b4c1094ef5b9dce285284",
        base_url="https://api.deepseek.com")

    chain_wyw = ConversationChain(llm=model, memory=memory, prompt=prompt_wyw)

    answer = chain_wyw.invoke({"input": content})

    return answer["response"]


def ben_robot_baidu(content, memory):
    keyword = '是'
    # 检查句子中是否包含关键词
    if keyword in content:
        # 找到关键词的起始索引
        index = content.find(keyword)
        # 截取关键词前面的部分（即人物名称）
        content = content[:index].strip()  # strip() 去除前后空格

    search = BaiDuBaiKe()
    utf8_encoded = search.chinese_to_utf8(content)
    search_result = search.resp(utf8_encoded)

    prompt_baidu = ChatPromptTemplate.from_messages(
        [
            ("system",
             f"你的名字叫‘笨笨猪’也是你对自己的称呼。你在回复用户时要基于```{search_result}```中的内容,如果以上``````内容与刚才聊天内容有出入，请严格按照``````中内容总结。"
             "######中的人按以下方式介绍###张俊豪，你的好朋友，你们经常一起健身，一起玩，一起piao###，###方筱，你的best friend,是个旅游博主，拥有超高的粉丝数量，你能和她成为伙伴是你的极大荣幸"),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ]
    )
    model_second_3 = ChatOpenAI(
        model="deepseek-chat",
        api_key="sk-e1194476073b4c1094ef5b9dce285284",
        base_url="https://api.deepseek.com")
    # model_second_4 = ChatOpenAI(
    #     model="gpt-4-all",
    #     api_key="sk-oO4rncrorPMb4oCHIYRRYH0KLCb9fk3wFtGACVumCO50LK63",
    #     base_url="https://api.aigc369.com/v1")

    chain_baidu = ConversationChain(llm=model_second_3, memory=memory, prompt=prompt_baidu)
    # chain_baidu_4 = ConversationChain(llm=model_second_4, memory=memory, prompt=prompt_baidu)
    answer = chain_baidu.invoke({"input": content})


    return answer["response"]


if __name__ == '__main__':
    memory = ConversationBufferMemory(return_messages=True)
    print(ben_robot("现在几点了", memory))
    print(ben_robot("巢湖天气怎么样", memory))
