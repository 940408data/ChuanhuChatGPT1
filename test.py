
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2023/06/06 15:56:14
@Author  :   huangxu3 
@Version :   1.0
@Contact :   huangxu3@newhope.cn
@License :   (C)Copyright 2021-2022, newhope.cn
@Desc    :   None
'''

# here put the import lib


import logging
import json
import commentjson as cjson
from modules.models.models import get_model
import colorama


with open("config.json", "r") as f:
        openai_api_key = cjson.load(f)["openai_api_key"]
#     # set logging level to debug
logging.basicConfig(level=logging.DEBUG)
# client = ModelManager(model_name="gpt-3.5-turbo", access_key=openai_api_key)
# # client = get_model(model_name="chatglm-6b-int4")
# chatbot = []
# stream = False
# # 测试账单功能
# logging.info(colorama.Back.GREEN + "测试账单功能" + colorama.Back.RESET)
# logging.info(client.billing_info())
# # 测试问答
# logging.info(colorama.Back.GREEN + "测试问答" + colorama.Back.RESET)
# question = "巴黎是中国的首都吗？"
# for i in client.predict(inputs=question, chatbot=chatbot, stream=stream):
#     logging.info(i)
# logging.info(f"测试问答后history : {client.history}")
# # 测试记忆力
# logging.info(colorama.Back.GREEN + "测试记忆力" + colorama.Back.RESET)
# question = "我刚刚问了你什么问题？"
# for i in client.predict(inputs=question, chatbot=chatbot, stream=stream):
#     logging.info(i)
# logging.info(f"测试记忆力后history : {client.history}")
# # 测试重试功能
# logging.info(colorama.Back.GREEN + "测试重试功能" + colorama.Back.RESET)
# for i in client.retry(chatbot=chatbot, stream=stream):
#     logging.info(i)
# logging.info(f"重试后history : {client.history}")


# # client = get_model(model_name="chatglm-6b-int4")
# client = ModelManager(model_name="gpt-3.5-turbo", access_key=openai_api_key)
# input_info = "3+5?"
model, msg, chatbot,update_info = get_model(model_name = "gpt-3.5-turbo", access_key = openai_api_key)
# print(model.predict())
# print(msg)

# chatbot_history = [("你好，你需要帮忙吗？", "成功")] 
# inputs = "今天天气怎么样？" 
# stream = False 
# use_websearch = False 
# files = ["索引.txt"] 
# reply_language = "中文" 
# should_check_token_count = True

# inputs_list = ["树木的定义","石头的定义"]
# #创建对象
# # assistant = WritingProgrammingAssistant() 
# result = model.predict(inputs = inputs, chatbot = chatbot_history)

# # 查看输出结果
# for res in result: 
# 	print(res)
        

# test_inputs = "你好"
# test_chatbot = [("你好，我是聊天机器人，有什么问题可以问我。", "success")]
test_stream = False
test_use_websearch = False
test_files = None
test_reply_language = "中文"
test_should_check_token_count = True
# #现在我们可以调用 predict 函数进行测试：

# for chatbot, status_text in model.predict(
#         test_inputs,
#         test_chatbot,
#         stream=test_stream,
#         use_websearch=test_use_websearch,
#         files=test_files,
#         reply_language=test_reply_language,
#         should_check_token_count=test_should_check_token_count
#     ):
#     print(chatbot)
#     print(status_text)



test_inputs = "你好"
test_chatbot = []
while True:
    response = input("聊天机器人回答：")
    if not response:
        break
    test_chatbot.append((response, ""))
# 现在我们可以使用新数据调用 predict 函数进行测试：

    for chatbot, status_text in model.predict(
            test_inputs,
            test_chatbot,
            stream=test_stream,
            use_websearch=test_use_websearch,
            files=test_files,
            reply_language=test_reply_language,
            should_check_token_count=test_should_check_token_count
        ):
        print(chatbot)
        print(status_text)