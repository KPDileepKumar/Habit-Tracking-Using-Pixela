import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "!#Pw8EcJ*C1u)Uc6F"
USERNAME = "dilip84"

GRAPH_ID = "graph1"

user_params = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {"X-USER-TOKEN": TOKEN}
graph_config = {"id": "graph1", "name": "Coding graph", "unit": "problems", "type": "int", "color": "momiji"}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today = datetime.now()
today_date = today.strftime("%Y%m%d")
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
add_pixel_configuration = {"date": today_date, "quantity": input("Enter the number of problems you solved: ")}
response = requests.post(url=add_pixel_endpoint, json=add_pixel_configuration, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
update_pixel_configuration = {"quantity": "5"}
# response=requests.put(url=update_pixel_endpoint,json=update_pixel_configuration,headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs{GRAPH_ID}/{today_date}"
# response=requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)
