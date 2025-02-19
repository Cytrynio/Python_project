import requests
from datetime import datetime


USERNAME = "cytrynox"
TOKEN = "a1eoi12einh0812334rt"
GRAPH_ID = "graph1"



pixela_endpoint ="https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_parameters)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Walking Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

graph1_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today().strftime("%Y%m%d")

pixel_data = {
    "date":today,
    "quantity":input("How many Km do you walked today?")
}

#
response = requests.post(url=graph1_endpoint, json=pixel_data, headers=headers)
print(response.text)

#
# updated_data ={
#     "quantity":"8"
# }
#
# # response=requests.put(f"{graph1_endpoint}/20250217",headers=headers,json=updated_data)
#
# response = requests.delete(f"{graph1_endpoint}/20250217",headers=headers)
#
# print(response.text)
# print(response.status_code)
#
