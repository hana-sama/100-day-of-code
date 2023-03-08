height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")
int_height = float(height)
int_weight = float(weight)
bmi = int_weight / (int_height * int_height)
round_bmi = round(bmi, 2)
if round_bmi >= 30:
    print(f"Your BMI is {round_bmi}. You're in the obese range")
elif 25 <= round_bmi <= 29.9:
    print(f"Your BMI is {round_bmi}. You're in the overweight range")
elif 18.5 <= round_bmi <= 24.9:
    print(f"Your BMI is {round_bmi}. You're in the healthy weight range")
else:
    print(f"Your BMI is {round_bmi}. You're in the underweight range")
