
# Read data into a list and convert the data to integers
with open("1_data_test.txt", "r") as data:
    data_list = data.read().split("\n")
data_list = data_list[:-1]
print(data_list)

values = []
j = 0
for entry in data_list:
    for i in range(len(entry)):
        try:
            if 0 <= int(entry[i]) and int(entry[i]) <= 9:
                print(int(entry[i]))
                values.append(entry[i])
        except:
            pass
print(values)
