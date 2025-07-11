List=["Ajay",20,"Male"]   #If we repeat a value inside list then a error will occur that too many unpacking like List=["Ajay",20,"Ajay","Male"] 
Name,Age,Gender=List
print(Name)
print(Age)
print(Gender)


print("--------------------------------" )


tuple=("Ajay",20,"Ajay","Male") #Here if we repeat it will automatically exclude repeated values after 1st value
Name,Age,Gender=List
print(Name)
print(Age)
print(Gender)

print("--------------------------------" )

set={"Ajay",20,"Ajay","Male"} #Here also if we repeat it will automatically exclude repeated values after 1st value
Name,Age,Gender=List
print(Name)
print(Age)
print(Gender)


print("--------------------------------" )

disc={"Ajay":"Good",20:"Years","Male":"M"} #Here also if we repeat it will automatically exclude repeated values after 1st value
Name,Age,Gender = disc             #disctionary is different becoz we can not do like "Ajay":"Good",20:"Years","Male":"M" in tuple
print(Name,disc.get(Name))
print(Age,disc.get(Age))
print(Gender,disc.get(Gender))
