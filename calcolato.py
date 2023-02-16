def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "//":
        return num1 // num2
    elif operator == "%":
        return num1 % num2
    elif operator == "^":
        return num1 ** num2
    else:
        return None

def get_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == "int":
                user_input = int(user_input)
            elif input_type == "float":
                user_input = float(user_input)
            elif input_type == "operator":
                if user_input in ["+", "-", "*", "/", "//", "%", "^"]:
                    return user_input
                else:
                    print("Invalid operator, please try again")
                    continue
            else:
                print("Invalid input type, please try again")
                continue
        except ValueError:
            print("Invalid input, please try again")
            continue
        else:
            return user_input

previous_calculations = []

while True:
    num1 = get_input("Enter the first number: ", "float")
    operator = get_input("Enter the operator (+, -, *, /, //, %, ^): ", "operator")
    num2 = get_input("Enter the second number: ", "float")

    result = calculate(num1, operator, num2)

    if result is None:
        print("Invalid operator, please try again")
        continue
    else:
        # Round the result to the nearest integer and convert to int
        result = int(round(result))

        # Store the calculation in a nested list
        calculation = [num1, operator, num2, result]
        previous_calculations.append(calculation)

        # Print the result
        print(f"{num1} {operator} {num2} = {result}")

    user_choice = input("Do you want to perform another calculation? (y/n): ")
    if user_choice.lower() == "y":
        continue
    elif user_choice.lower() == "n":
        break
    else:
        print("Invalid input, please try again")
        continue

# Print the previous calculations
print("\nPrevious calculations:")
for calculation in previous_calculations:
    print(f"{calculation[0]} {calculation[1]} {calculation[2]} = {calculation[3]}")

#by_mohamed_galal