# while first_number == '':
#     print("first number cannot be empty")
#     first_number = input(first_number)

def input_validation(number):
    while True:
        try:
            input_number = int(input(number))
        except ValueError:
            print("number is invalid")
            continue
        else:
            return input_number
            break


first_number = input_validation("Enter first number")
print(f"First number {first_number}")

second_number = input_validation("Enter second number")
print(f"Second number {second_number}")

total = int(first_number + second_number)

print(f"Total is {total}")
