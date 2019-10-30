print("code for problem-3\n")

value=[]
numbers=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
print("main list :",numbers)

for i in range(len(numbers)):
	if numbers[i]==2:
		value.append(i)

print(value)

