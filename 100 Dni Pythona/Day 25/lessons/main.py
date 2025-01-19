# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatues = []
#     for row in data:
#         if row[1] != "temp":
#             int_temp = int(row[1])
#             temperatues.append(int_temp)
#     print(temperatues)

import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # #
# data_dict = data.to_dict()
# #
# data_list = data["temp"].to_list()
# avg_temperature = round(sum(data_list) / len(data_list), 1)
# # print(avg_temperature)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())\


# print(data[data.temp == data["temp"].max()])


# monday = data[data.day == "Monday"]
#
# print((monday.temp* 9 / 5) + 32)

#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

wynik = data.groupby('Primary Fur Color').size()

wynik.to_csv("Ilosc wiewiórów.csv")


