import json

import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print('1)', response1.text)
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "HEAD"})
print('2)', response2.text)
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print('3)', response3.text)

wrong_answer = '4) wrong response; request: {}, method: {}, but response: {}'
methods = ["GET", "POST", "DELETE", "PUT"]

for method in methods:
    response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": method})
    response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
    response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})
    response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": method})

    if response_get.text == '{"success":"!"}' and method != "GET":
        print(wrong_answer.format("get", method, response_get.text))
    elif response_get.text != '{"success":"!"}' and method == "GET":
        print(wrong_answer.format("get", method, response_get.text))

    if response_post.text == '{"success":"!"}' and method != "POST":
        print(wrong_answer.format("post", method, response_post.text))
    elif response_post.text != '{"success":"!"}' and method == "POST":
        print(wrong_answer.format("post", method, response_post.text))

    if response_delete.text == '{"success":"!"}' and method != "DELETE":
        print(wrong_answer.format("delete", method, response_delete.text))
    elif response_delete.text != '{"success":"!"}' and method == "DELETE":
        print(wrong_answer.format("delete", method, response_delete.text))

    if response_put.text == '{"success":"!"}' and method != "PUT":
        print(wrong_answer.format("put", method, response_put.text))
    elif response_put.text != '{"success":"!"}' and method == "PUT":
        print(wrong_answer.format("put", method, response_put.text))