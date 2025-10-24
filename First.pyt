# Calculate how many days in your life

name = str(input("Please Enter Your First Name : "))
print("Welcome Sir")
consent = str(input("Do you want to know your age in days ? "))
if consent == "okay" :
    age = float(input("Please Enter Your Age : "))
    year = age * 365
    month = year / 12
    hour = year * 24
    print('year :',year)
    print('month : ',month)
    print('hour : ',hour)
else :

    print("I,m Sorry!")
