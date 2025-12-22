info = {
    "key" : "value",
    "name" : "Rahaab",
    "subject" : ["Python", "C","Java"],
    "topics" : ("dictionary", "set"),
    12 : 66,
    "Learning" : "Python",
    "age" : 35,
    "Adult" : True,      
    "marks" : 94.4 ,

}

# print(type(info))

# print(info["name"])
# print(info["topics"])
# print(info["marks"])

# info["name"] = "Rahaab Ahmed"
# print(info)

# info["surname"] = "Ahmed"
# print(info)

null_dict = {}
null_dict["name"] = "Rahaab"
print(null_dict)
 
 ------------------Nested dictionary-------------------------------
student = {
    "name" : "rahul kumar",
    "subjects" :
    {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

#nested dictionary
print(student["subjects"]["chem"])

-----------------------dictionary methods-----------------------
 
print(myDict.keys()) #returns all keys

myDict.values() #returns all values

myDict.items() #returns all (key, val) pairs as tuples

myDict.get( "key" ) #returns the key according to value

myDict.update( newDict ) #inserts the specified items to the dictionary