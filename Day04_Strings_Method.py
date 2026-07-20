# strings are immutable
name = "vishal varma!!!!!!"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.rstrip("!"))
print(name.replace("vishal", "neha"))
print(name.split(" "))
print(name.center(36))
print(name.count("v"))
print(name.swapcase()) #Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(name.title()) #More specifically, words start with uppercased characters and all remaining cased characters have lower case.
print(name.endswith("!"))
print(name.startswith("vishal")) 
print(name.endswith("al", 2, 6)) #Return True if the string ends with the specified suffix, False otherwise.
print(name.isalnum()) #Return True if the string is an alphanumeric string, False otherwise.
print(name.isalpha()) #Return True if the string is an alphabetic string, False otherwise. (It does not include numbers and special characters.)
string = "He's name is vishal"
print(string.find("is")) #Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
print(string.index("is")) #Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.
print(string.islower()) #Return True if the string is a lowercase string, False otherwise.
print(string.isprintable()) #some strings can't be printed like \n that creats second lines.
print(string.isspace()) #Return True if the string is a whitespace string, False otherwise.
print(string.istitle()) #if in your strings each word's first letter is capitle then it is 'true' otherwise 'false'