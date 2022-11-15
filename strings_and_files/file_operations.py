# f = open("text.txt")
# lines = f.readlines()
# print(lines)
# f.close()

with open("text.txt") as f:
    lines = f.readlines()

total_sum = 0
for number in lines:
    total_sum += int(number)
print(total_sum)


with open("text.txt") as f:
    sum = 0
    for line in f.readlines():
        sum += int(line)
    print(sum)