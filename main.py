import csv

#Using csv module to work with data
with open("/Users/emre/Documents/Code/100DaysOfPython/Day21-30/Day25/weather_data.csv") as file:
    data = file.readlines()
    print(data)

with open("/Users/emre/Documents/Code/100DaysOfPython/Day21-30/Day25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

#Using pandas module to work with data
import pandas

data = pandas.read_csv("/Users/emre/Documents/Code/100DaysOfPython/Day21-30/Day25/weather_data.csv")
print(data["temp"])
print(data)
#each column is a series in pandas
#the whole table will be a dataframe in pandas

#Converting to data to dictionary and adding the temperatures to a list
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

#Calculating the average with and without pandas:
sum_temp = sum(temp_list)
avg = sum_temp / len(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
#We get hold of the dataframe(table), and within sqaure brackets we choose the name of the column to get the entire column
print(data.condition)
print(data["condition"]) 

#Get data in rows
#We get hold of the dataframe(table), get a hold of the column and then give it a condition to get that entire row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Getting specific data from a row
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp
monday_temp_f = (monday_temp * 9/5) + 32
print(monday_temp_f)

#Create a Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Emre"],
    "scores": [76, 56, 65],
}

#Exporting python dictionary to csv file
data = pandas.DataFrame(data_dict)
data.to_csv("new_fileData.csv")


