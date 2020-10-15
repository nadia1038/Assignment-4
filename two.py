#2. Write a Python program to count the number of characters (character frequency) in a string.

#Sample String: google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

string = "google.com"
countg = 0
counto = 0
countl = 0
counte = 0
countd = 0
countc = 0
countm = 0

for i in range(len(string)) :
    if string[i]=='g':
        countg += 1
for i in range(len(string)) :
    if string[i]=='o':
        counto +=1
for i in range(len(string)) :
    if string[i]=='l':
        countl +=1
for i in range(len(string)) :
    if string[i]=='e':
        counte +=1
for i in range(len(string)) :
    if string[i]=='.':
        countd +=1
for i in range(len(string)) :
    if string[i]=='c':
        countc +=1
for i in range(len(string)) :
    if string[i]=='m':
        countm +=1
        
        
print("'g' :",countg,"'o':",counto ,"'l':",countl ,"'e':",counte ,"'.':",countd ,"'c':",countc ,"'m':",countm)


#AlternativeWay

string=input()
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
counta=0
countb=0
countc=0
countd=0
counte=0
countf=0
countg=0


for i in string:
    if i==a:
        counta+=1
for i in string:
    if i==b:
        countb+=1
for i in string:
    if i==c:
        countc+=1
for i in string:
    if i==d:
        countd+=1
for i in string:
    if i==e:
        counte+=1
for i in string:
    if i==f:
        countf+=1
for i in string:
    if i==g:
        countg+=1
       
print("'g' :",counta,"'o':",countb ,"'l':",countc ,"'e':",countd ,"'.':",counte ,"'c':",countf ,"'m':",countg)
