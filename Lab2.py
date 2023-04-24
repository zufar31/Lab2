print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi =float(weight/(height*height))
    print("bmi = " +str(bmi))
    if (bmi<18.5):
        print("UW")
    elif (18.5 <= bmi <= 25.0):
        print ("N")
    else:
        print("OW")

calculate_bmi(weight=50, height=1.65)


