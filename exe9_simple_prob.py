def calculate_simple_probability():
    try:
        favorable = float(input("Enter number of favorable outcomes: "))
        possible = float(input("Enter total number of possible outcomes: "))

        if possible == 0:
            print("Error: Total outcomes cannot be zero")

        elif favorable < 0 or possible < 0:
            print("Error: Outcomes cannot be negative numbers.")

        elif favorable > possible:
            print("Error: Favorable outcomes cannot be greater than total outcomes.")

        else:
            probability = favorable / possible
            percentage = probability * 100

            print(f"\nResults:")
            print(f"Probability: {probability:.4f}")
            print(f"Percentage: {percentage:.2f}%")

    except ValueError:
        print("Error: Please enter valid numbers only.")

calculate_simple_probability()
