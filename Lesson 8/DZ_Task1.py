"""Implement a program to calculate a person's body mass index."""

try:

    height = float(input("Please enter your height (in meters): "))
    print(float(height))



    weight = int(input("Please enter your weight: "))
    print(int(weight))

    body_index = weight / (height **2)
    # print(f"Your body index is:{body_index}")
    if body_index < 18.5:
        print(f"Body weight deficiency ")
    elif 18.5 <= body_index <= 25:
        print((f"Your body index is fine:{body_index}"))
    elif 25 < body_index <=30:
        print((f"Overweight (pre-obesity):{body_index}"))
    elif body_index > 30:
        print(f"Your are fat! Go to the doctor:{body_index}")


except ValueError:
    # мы не должны вводить буквы или запятую
    print("Error! Input only numbers. For fractions, use a period..")