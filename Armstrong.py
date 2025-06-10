# Take a 3-digit number from the user
num = int(input("Enter a 3-digit number: "))

# Check if it's a 3-digit number
if 100 <= num <= 999:
    # Separate the digits
    temp = num
    sum_of_cubes = 0

    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10

    # Check if the number is an Armstrong number
    if sum_of_cubes == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
else:
    print("Please enter a valid 3-digit number.")
