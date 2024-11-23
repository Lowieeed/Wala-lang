count = 0
while True:
    count += 1
    print(f"\nPerson {count}:")

    # Input for the user's weight, height, and age
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    age = int(input("Enter your age: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine the health risk based on BMI and age
    if bmi < 18.5:
        if age < 18:
            print("Underweight (Low Risk)")
        elif age <= 50:
            print("Underweight (Moderate Risk)")
        else:
            print("Underweight (High Risk)")
    elif 18.5 <= bmi <= 24.9:
        print("Healthy Weight (Low Risk)")
    elif 25 <= bmi <= 29.9:
        if age < 18:
            print("Overweight (Moderate Risk)")
        elif age <= 50:
            print("Overweight (High Risk)")
        else:
            print("Overweight (Very High Risk)")
    else:
        print("Obese (Very High Risk)")

    # Ask the user if they want to continue
    continue_input = input("Do you want to enter details for another person? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break
