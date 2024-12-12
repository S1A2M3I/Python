#BMI formula
height = float(input("Enter your height in centeimeters: "))
if height > 240:
    print("Invalid height")
else:
    weight = float(input("Enter your weight in kilograms: "))
    if weight > 180:
            print("Invalid weight")
    else:
            bmi = weight / (height ** 2)
            if bmi <= 18.5:
                print("Underweight")
            elif bmi <= 25:
                print("Normal")
            elif bmi <= 30:
                print("Overweight")
            else:
                print("Obese")