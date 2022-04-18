import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()<>?/+_"
while(True):
    len_p = int(input("Enter the length for the password (min 8): "))
    if len_p >= 8:
        p = "".join(random.sample(password,len_p))
        print(f"Your password is {p}")
        break
    else:
        print("Enter a length more than 8.")


