number = []
new_number = 1
sum = 0
sum_index = 0
max_number = float('-inf')

print("Enter a list of numbers, type 0 to stop: ")
while new_number != 0:
    new_number = int(input("Enter number: "))
    if new_number != 0:
        number.append(new_number)

for i in range(len(number)):
    sum += int(number[i])
    sum_index = i + 1
    if number[i] > max_number: 
            max_number = number[i]
    average = sum / sum_index
print(f"The sum of the numbers is: {sum}")
print(f"The average of the numbers is: {average}")
print(f"The largest number is: {max_number}")