# -*- coding: utf-8 -*-
"""pyt-practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nGUi-ukCCFtOcVnDx7iH4S280wFKeZWe
"""

n=8
for i in range(1,9,1):
  if(n%i==0):
    print("number divisible",i)

i=1
num=8
while(i<=num):
  if(num%i==0):
    print("number divisible",i)
  i=i+1

n=int(input("enter a number"))
for i in range(1,10):
  if(n%i==0):
    print(i)

num=9
age=0
for i in range(2,num):
  if(num%i==0):
    print("not a prime number",i)
    age=1
    break
  else:
    print("this is a prime number",i)
print("outside statement=>",age)

num=9
age=0
for i in range(2,num):
  if(num%i==0):
    print("not a prime number",num)
    age=1
    break

if(age==0):
  print("prime number",num)

num=27
for i in range(2,11):
  if num%i==0:
    print(i)
    break

total=0
num=40
for i in range(1,41):
  if(num%i==0):
    print(i)
    total+=i
print(total)

