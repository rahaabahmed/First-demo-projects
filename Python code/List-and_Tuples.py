# -------------Practice Work------------

# # ------------ASKING USER OF HIS 3 favourite movies-------------]
# M = []
# # l1 = input("Enter your 1st favourite movie :")
# # l2 = input("Enter your 2nd favourite movie :")
# # l3 = input("Enter your 3rd favourite movie :")

# # M.append(l1)
# # M.append(l2)
# # M.append(l3)
# # print(M)

# # --OR--

# M.append(input("Enter your 1st Favourite movie :"))
# M.append(input("Enter your 2nd Favourite movie :"))
# M.append(input("Enter your 3rd Favourite movie :"))
# print(M)


# -------------------To check if list is palindrome or not-------------------------------------

L1 = ["m","a","a","m"]

copyL1 = L1.copy()
copyL1.reverse()

if(L1 == copyL1):
    print("YES its a palindrome")
else:
    print("No its not a palindrome")    




L2 = ["r","a","c","e","f","a","r"]

copyL2 = L2.copy()
copyL2.reverse()

if(L2 == copyL2):
    print("YES its a palindrome")
else:
    print("No its not a palindrome")  

# ------------------Count the students With grade A--------------------

student_grades = ["C", "D", "A", "A", "B", "B", "A"]

print(student_grades.count("A"))

# ----------------take numerics data and Store in acending order------------------------

data = [] 
data.append(input("Enter 1st number :"))
data.append(input("Enter 2nd number :"))
data.append(input("Enter 3rd number :"))
print(data)
data.sort()
print(data)


















# --------------Concepts--------------------------

# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# # ______Python lists can hold data of multile data types in a single list 

# student = ["Rahaab", 18 ,"Lahore"]

# print("Name of the students is", student[0] ,"and age is" ,student[1] ,".","He lives in",student[2],"." )
   


# #    ----------note-----------

# In list we can change entities by index number septerately but 
# in simple variable strings we can not change the specific entity by index number 

# ------------This thing is not possible ----------------
# str = "hello"
# print(str[0])
# str[0] = "y"
  
#-------but this possible----------- 
#         #   0      1      2
# str = ["haadi", 18 , "lahore"]
# print("Name of the students is", str[0] ,"and age is" ,str[1] ,".","He lives in",str[2],"." )

# str[0],str[1] = "Rahaab",17 
# print("Name of the students is", str[0] ,"and age is" ,str[1] ,".","He lives in",str[2],"." )

# _______Slicing in list _________

# marks = [87, 64, 33, 95, 76]

# marks[1:4]      # [64, 33, 95]
# print(marks[1:4]) # ending index include nhi hota 
# print(len(marks))    #total number of elements
# marks[:4]       # same as marks[0:4]

# marks[1:]       # same as marks[1:len(marks)]

# marks[-3:-1]    # [33, 95]


# -------------------List methods-----------------------------

# list = [2, 1, 3]
# l = ["a", 'd' ,'b' ,'c' , 'f' ,'e']

# # list.append(4) #adds one element at the end   [2, 1, 3, 4]
# # l.append("g") #adds one element at the end   [2, 1, 3, 4]
# print(list)
# print(l)

# l.sort( ) #sorts in ascending order    a b c d
# list.sort( ) #sorts in ascending order   [1, 2, 3]
# print(l)
# print(list)


# list.sort( reverse=True ) #sorts in descending order   [3, 2, 1]
# l.sort( reverse=True)
# print(l)
# print(list)


# list.reverse( ) #reverses list   [3, 1, 2] and this is ""PERMANENT""" change in list
# l.reverse()
# print(list)
# print(l)



# list.insert( 3, 99 ) #insert element at index ,and this is ""PERMANENT""" change in list
# l.insert(  3, "W")
# print(list)
# # print(l)
 

# list = [2, 1, 3, 1]

# list.remove(1) #removes first occurrence of element  [2, 3, 1]

# list.pop( 1 ) #removes element at 1(specified index)
# print(list)



list = [2, 1, 3]

new_list = list.copy() #returns a shallow copy of the list  [2, 1, 3]


# ---------------------Tuples---------------------

# tup = (5,6,7,8)    #unchangable thing
# print(tup)

# # tup[0] = 2      #assigning is not allowed
# # tup = (1)   wrong
# tup = (1,)  #correct
# print(type(tup))


# # 

# tup = (2, 1, 3, 1)

# tup.index( 1 ) #returns index of first occurrence   tup.index(1) is 1

# tup.count( el ) #counts total occurrences   tup.count(1) is 2