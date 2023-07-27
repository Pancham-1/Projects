
print(" **** BMI CALCULATOR **** ")
weight = float(input(" Please tell your weight (in kg) : "))
height = float(input(" Please tell your height (in cm) : "))
bmi = weight*100**2/height**2
if bmi<16:
    print(f"You're SEVERLY UNDERWEIGHT with BMI of {bmi}. Set up a routine to eat and drink things you like and that have a lot of nutrients as well as calories")
elif bmi<18.4:
    print(f"You're UNDERWEIGHT!!! with BMI of {bmi}")
elif bmi<24.9:
    print(f"Yes!!!! You're Healthy with BMI of {bmi}")
elif bmi<29.9:
    print(f"You're OVERWEIGHT with BMI of {bmi}")
elif bmi<34.9:
    print(f"You're OBESE !!! with BMI of {bmi} ")
elif bmi<39.9:
    print(f"You're SVERELY OBESE !!! with BMI of {bmi}  ")
else:
    print(f"You're MORBIDLY OBESE with BMI of {bmi}. Choose healthier foods (whole grains, fruits and vegetables, healthy fats and protein sources) and beverages. Limit unhealthy foods (refined grains and sweets, potatoes, red meat, processed meat) and beverages (sugary drinks). Increase physical activity.")

# This exercise taught me how to use BMI chart with the help of if, elif statements to make a BMI calculator.
