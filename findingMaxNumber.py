# creating an empty list
numbers = []

# for loop defined for taking 5 numbers from user
for i in range(1, 6):
    number = int(input(f'Enter {i}. number : '))
    numbers.append(number)

# finding max number in the created list
# first element assigned as a maximum number for comparison
max_number = numbers[0]

for i in range(5):
    if numbers[i] > max_number:
        max_number = numbers[i]

# for debuging the list
# print(numbers)

# displays the result
print(f'Maximum number of the given list is {max_number} !!!')
