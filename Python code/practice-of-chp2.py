# ----------------input user name and print its Length-----------------------

# n = input("Enter your name :")
# print("length =",len(n))

# -----------------Find the occurance of  $ sign ------------------------

# s = input("Enter your string :")
# print(s.count("$"))

# -------------------------if-elif-else------------------------------------------------------
# m = int(input("Enter your percentage in exam :"))

# if(m >=90):
#     print("Grade is A")
# elif(m>=80):    
#     print("Grade is B")
# elif(m>=70):
#     print("Grade is C")
# elif(m>=60):  
#     print("Grade is D")
# elif(m>=50):  
#     print("Grade is E")
# elif(m>=33 and m < 50):    
#     print("Grade is F")
# else:
#     print("Invalid Input")    

# --------------if the number is even or odd------------------------------

# n = int(input("Enter any number :"))

# if(n % 2 == 0):
#     print("Even")
# else:
#     print("Odd")    


# ---------------to find greatest of three number----------------------

# n1 = int(input("Enter 1st number :")) 
# n2 = int(input("Enter 2nd number :")) 
# n3 = int(input("Enter 3rd number :")) 

# if(n1 > n2 and n1 > n3 ):
#     print("Greatest number is",n1)
# elif(n2 > n1 and n2 > n3):
#     print("Greatest number is",n2)    
# elif(n3 > n1 and n3 > n2):
#     print("Greatest number is",n3)    
# else:
#     print("Numbers are Equal or Invalid Input")   

# __________________multiple of 7 or not______________________________

n = int(input("Enter a number :"))

if(n % 7 == 0):
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")    