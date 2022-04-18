#Character and String objects
# '<single_character>' denotes a character "<multiple_characters>" denotes a string
char1 = 'a'

print("==============================================================================")
print("Basic output")
#Basic output
print(char1)
print("==============================================================================")

print("==============================================================================")
print("Concatenating string objects + operator: String3 = \"String1\" + \"String2\"")
#Combining string type objects with other string type objects doesn't require any
#conversion
print("char1: " + char1)

string1 = "Artificial"
print(string1)
print("string1: " + string1)
string2 = "Intelligence"
print(string2)
print("string2: " + string2)

#Concatenating string objects
# + operator: String3 = "String1" + "String2"
string3 = "String1" + "String2"
print(string3)
print("string3: " + string3)
string3 = string1 + string2
print(string3)
print("string3: " + string3)

#Better to add some space to make it more appealing
string3 = string1 + ' ' + string2
print(string3)
print("string3: " + string3)
print("==============================================================================")

print("==============================================================================")
print("Swapping values between two objects")

#Swapping values between two string objects
print("\nValues of string1 and string2 before swap")
print("string1: " + string1)
print("string2 = " + string2)
string1, string2 = string2, string1
print("\nValues of string1 and string2 after swap")
print("string1: " + string1)
print("string2: " + string2)
print("==============================================================================")

print("==============================================================================")
print("Accesing any character in a string")
#Accesing any character in a string
print("string3[4]: "  + string3[4])
print("==============================================================================")

