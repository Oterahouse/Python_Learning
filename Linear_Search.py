import random

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break

    return found

# numbers = range(0, 100)
numbers = []
for number in range(0,51):
    ran = random.randint(0,100)
    numbers.append(ran)

print(str(numbers) + "\n")
s1 = ss(numbers, 2)
print(s1)

s2 = ss(numbers, 50)
print(s2)