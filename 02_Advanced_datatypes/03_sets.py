#SET in python
snacks1={"Samosa","Vadapav","Chowmin","Sambhar-vada"}
print(snacks1)
print(type(snacks1)) # set is a built-in data type in Python
print(id(snacks1))
snacks1.add("Dabeli") # adding an element to the set
print(id(snacks1)) # set is mutable data type in Python
snacks1.add("Samosa") # adding a duplicate element to the set
print(snacks1) # set does not allow duplicate elements
snacks1.remove("Chowmin") # removing an element from the set
print(snacks1)
snacks2={"Chips","Kurkure","Samosa","Chowmin","Aloo-Petty"}
print(snacks1 | snacks2) # union of two sets
print(snacks1 & snacks2) # intersection of two sets
print(snacks1 - snacks2) # difference of two sets
print(snacks1 ^ snacks2) # symmetric difference of two sets

