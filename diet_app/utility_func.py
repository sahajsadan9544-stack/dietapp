#BMR for men:
# (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) + 5

#BMR for women:
# (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) + 161


def calculate_bmr(age, weight, height, gender, activity_level):
    bmr=0
    if gender=="male":
        bmr = (10*weight) + (6.25*height) - (5*age) + 5
    else:
        (10*weight) + (6.25*height) - (5*age) + 161
    tdee=bmr*float(activity_level)
    return tdee

d=calculate_bmr(28, 80, 180, "male", 1.2)
print(d)