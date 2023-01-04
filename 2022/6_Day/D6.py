with open('6_data.txt', 'r') as file:
    char_stream = file.read().splitlines()

chars = char_stream[0]
print(char_stream)

# print out the string in groups of 100
for i in range(100,len(chars),100):
    print(chars[i-100:i+1])

# find the first group of 4 that has all unique characters
for i in range(3,len(chars)):
    if len(set(chars[i-3:i+1])) == len(chars[i-3:i+1]):
        print(i + 1)
        print(chars[i-3:i+1])
        break

# find the first group of 14 that has all unique charachers
for i in range(13,len(chars)):
    if len(set(chars[i-13:i+1])) == len(chars[i-13:i+1]):
        print(i + 1)
        print(chars[i-13:i+1])
        break

