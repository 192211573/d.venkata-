def main():
    positive_numbers = []
    negative_numbers = []
    
    print("Enter -1 to exit...")
    
    while True:
        try:
            number = float(input("Enter the number: "))
            if number == -1:
                break
            elif number > 0:
                positive_numbers.append(number)
            elif number < 0:
                negative_numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if positive_numbers:
        avg_positive = sum(positive_numbers) / len(positive_numbers)
    else:
        avg_positive = 0.0
        
    if negative_numbers:
        avg_negative = sum(negative_numbers) / len(negative_numbers)
    else:
        avg_negative = 0.0
    
    print(f"The average of negative numbers is: {avg_negative:.2f}")
    print(f"The average of positive numbers is: {avg_positive:.2f}")

# Run the main function
main()

