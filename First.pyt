# Calculate how many days in your life

name = str(input("Please Enter Your First Name : "))
print("Welcome Sir")
consent = str(input("Do you want to know your age in days ? "))
if consent == "okay" :
    age = float(input("Please Enter Your Age : "))
    year = age * 365
    print(year)
else :
    print("I,m Sorry!")