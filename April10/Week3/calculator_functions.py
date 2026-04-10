def add_numbers(first_input, second_input):
    return first_input + second_input

value_one = float(input("Enter first number: "))
value_two = float(input("Enter second number: "))

sum_result = add_numbers(value_one, value_two)

print("Sum:", sum_result)