def calculate():
    while True:
        print("\n----**********----")
        print("Simple Calculator")
        print("----**********----")
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            choice = input("Enter the operation: ")

            if choice == '1' or choice == '+':
                result = num1 + num2
                print(f"\nResult: {result}")
            elif choice == '2' or choice == '-':
                result = num1 - num2
                print(f"\nResult: {result}")
            elif choice == '3' or choice == '*':
                result = num1 * num2
                print(f"\nResult: {result}")
            elif choice == '4' or choice == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"\nResult: {result}")
                else:
                    print("\nError!!Division by zero is not allowed!!")
            else:
                print("\nInvalid!! Please choose valid operations!!")

        except ValueError:
            print("\nError!!! Please enter valid numbers!!!")

        if input("\nDo another calculation? (y/n): ").lower() != 'yes':
            break


if __name__ == "__main__":
    calculate()
