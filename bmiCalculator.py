print("TO CALCULATE YOUR BMI INDEX, FILL THE INFORMATION BELOW")
while True:
    try:
        height = float(input("Enter your height (cm): "))
        assert height > 0
        break
    except ValueError:
        print("Please, enter a digit!")
    except AssertionError:
        print("Your height must surely be more than 0. Try again!")

while True:
    try:
        weight = float(input("Enter your weight (kg): "))
        assert height > 0
        break
    except ValueError:
        print("Please, enter a valid digit!")
    except AssertionError:
        print("Your weight must surely be higher than 0. Try again!")

bmi = (weight/height**2)*10000
bmi_rounded = round(bmi,2)

if (bmi >=19) and (bmi <=25):
    print(f"Your BMI index is '{bmi_rounded}' which is within average \nYou are fit. Keep it up!")
elif (bmi <19) and (bmi >=15):
    print(f"Your BMI index is '{bmi_rounded}' which is below average \nHmm, maybe you should eat more")
elif bmi <15:
    print(f"Your BMI index is '{bmi_rounded}' which is way below average \nI am concerned. You got anorexia bro?")
elif (bmi >25) and (bmi <=30):
    print(f"Your BMI index is '{bmi_rounded}' which is above average \nBetter hit the gym!")
else:
    print(f"Your BMI index is '{bmi_rounded}' which is way above average \nBad news: You are morbidly obese")
