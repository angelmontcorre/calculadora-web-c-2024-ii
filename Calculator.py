class Calculator:
    def __init__(self):
        self.operations = Operations()  # Instancia de la clase Operations

    def run(self):
        print("Welcome to the Calculator!")
        while True:
            print("\nSelect an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("Enter your choice (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    print(f"The result of adding {num1} and {num2} is: {self.operations.add(num1, num2)}")
                elif choice == '2':
                    print(f"The result of subtracting {num2} from {num1} is: {self.operations.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result of multiplying {num1} and {num2} is: {self.operations.multiply(num1, num2)}")
                elif choice == '4':
                    result = self.operations.divide(num1, num2)
                    print(f"The result of dividing {num1} by {num2} is: {result}")
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()