password=input("Enter your Password")
has_number=False
has_upper=False
for ch in password: #using for loop
    if ch.isdigit():
        has_number=True
    if ch.isupper():
        has_upper=True
if (len(password)>=8 and has_number and has_upper):
    print("password is updated")       
else:
    print("password must contain :")    
    print("minimum 8 characters")
    print("1 number")
    print("1 uppercase")
