a = []

# List of int with user input

number = int(input("Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Sorted list: ", a)