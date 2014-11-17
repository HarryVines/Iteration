largest_number = 0
number = int(input("Please enter a number in the series: "))

while (number != -1):
    number = int(input("Please enter a number in the series: "))
    if number > largest_number:
        largest_number = number

print("The largest number is {0}".format(largest_number))
