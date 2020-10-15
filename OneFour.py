#1. Write a Python program to calculate the length of a string

String = "abcdefghijklmnopqrstuvwxyz"

print(len(String))



#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

#Sample String: 'restart'
#Expected Result: 'resta$t'

string="restart"
array=[]
new_string=""

for i in string:
    array.append(i)
array[5]='$'

for i in array:
    new_string +=i
print(new_string)
