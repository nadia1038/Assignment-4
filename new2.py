#Take two string from console. And find those characters who are common in both strings.

##Sample input 1: "google" 
##Sample input 2: "facebook"
#output: o, e

string1=input()
string2=input()
array=[]
for i in string1:
    if (i in string2)and(i not in array):
        array.append(i)
print(array)

##Assignment 03
##-------------
##Take two string from console. And find those characters who are not common in both strings.
##
##Sample input 1: "google"
##Sample input 2: "facebook"
##output: g, l, f, a, c, b, k

string1 = input()
string2 = input()
array = []

for i in string1:
    if (i not in string2)and(i not in array):
        array.append(i)
for i in string2:
    if (i not in string1)and(i not in array):
        array.append(i)
        
print(array)        
