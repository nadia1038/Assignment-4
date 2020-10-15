##Take string from console. And find all unique characters.
##
##sample input: "unique"
##output: u, n, i, q, e

string=input()
array=[]

for i in string:
    if (i in string) and (i not in array):
        array.append(i)
print(array)


##sample input: "google"
##output: g, o, l, e

string=input()
array=[]

for i in string:
    if (i in string) and (i not in array):
        array.append(i)
print(array)
