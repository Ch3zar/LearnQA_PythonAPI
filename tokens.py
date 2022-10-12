import requests
import json
import time

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json_create_task = json.loads(create_task.text)
token_task = (json_create_task["token"])
seconds = (json_create_task["seconds"])
print("Получаю токен и секунды созданной задачи:", token_task, seconds)
token = token_task

check_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
json_check_task = json.loads(check_task.text)
status_check = (json_check_task["status"])
print("Проверяю статус задачи до создания:", status_check)

if status_check == "Job is NOT ready":
    time.sleep(int(seconds)+1)
    complete_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    json_complete_task = json.loads(complete_task.text)
    complete_task_status = (json_complete_task["status"])
    complete_task_result = (json_complete_task["result"])
    if complete_task_status == "Job is ready":
        print("Задача создана")
        if complete_task_result:
            print("Есть результат")
        else:
            print("Нет результата")
    else:
        print("Ошибка создания задачи")
else:
    print("Ошибка создания задачи")
