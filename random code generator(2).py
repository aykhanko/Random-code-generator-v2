import random
import string


symbols = string.ascii_letters

numbers = string.digits

punctations = string.punctuation


while True:

    print("Close the prgram(Input 0)")
    print("Choose code length(Min:8 Max:100):")

    try:

        count=int(input(""))

        if count==0:
            print("Program Closed")

            break

        elif count<8: 
            print("Less than 8!")

        elif count>100:
            print("More than 100!")

        else:

            code = ""

            for _ in range (count):
                
                rd_code=random.choice(symbols + numbers + punctations)
                
                code+=rd_code

            print("    Your code:",code)

            continue
                

    except ValueError:
        print("Input number!")

