from tabulate import tabulate
from prettytable import PrettyTable
from texttable import Texttable
import mypack.name
from mypack import name
from mypack.name import print_name
import random
from pathlib import Path
# from random import random

# x = int(input("Insert a number"))
# x = 10000
# print("x: "+str(x))
# y=4
# def isBigger(x,y):
#   if x>y:
#     return True
#   else:
#     return False

# print(isBigger(x,y))
# msg = 'hello there'

# for c in msg:
#   print(c,end="")
# print()
# for i in range(len(msg)):
#   print(msg[i],end="")
# print()


# def first_missing_positive(nums): 
#   for i in range(len(nums)+1):
#     for j in nums:
#       # print(str(i)+" "+str(j))
#       if (i>0 and j>0):
#         # print("---")
#         if i>j:
#           return i
#       # if i==j:
#         # print(i)
#   return -1
 
# nums = [3, 4, -1, 1]
# print(nums)

#strings
# print("================== Strings ====================")
# formatedstring = f"the array is {nums} and the result is {first_missing_positive(nums)}"
# print(formatedstring)

# print(formatedstring.upper())
# print(formatedstring.find("is"))
# print(formatedstring.replace("array","integer vector"))
# print("h" in msg)
# print("2" in msg)
# # in operator returns a boolean value ?
# print(msg.title())

# str1="strings"
# str2="numbers"
# print(str(len(str1))+" "+str(len(str2)))
# print(str(len("strings"))+" "+str(len("numbers")))

# numbers
# print("================== Numbers ====================")

# print(22/3) # float
# print(22//3) # int  
# print(2**6) # exponent
# print(round(2.5000000000000001))
# print(round(2.500000000000001))
# print(abs(-16))


# # num = input("insert a number: ")
# num = 4
# print(num+1)
# for i in range(2001,1,-200):
#   print(i,end=" ")
# print
# array = range(20)[:8]
# print(array)

# for i in array:
#   print(array[i],end=" ")
# print()
matrix = [[1,2,3],[2,3,1],[3,1,2]]
# for i in matrix:
#   for j in i:
#     print(j,end=" ")
#   print()
# print()
# print()

# for i in matrix:
#   print(i)
# print()
# print(matrix)

print(tabulate(matrix))
print()
print(PrettyTable(matrix))

#other
# print("================== Others =====================")

# fi = open("in.txt","r")
# strNr = str(fi.read())
# print(strNr)
# flag = False
# listNr = []
# for i in strNr.split():
#   try:
#     listNr.append(int(i))
#   except Exception:
#     flag=True
# if flag==True:
#   print("Some input data was invalid!")
# elif flag==False:
#   print("File succesfully read!")

# listNr2 = listNr.copy()
# listNr2.clear()
# for i in range(0,len(listNr),2):
#   listNr2.append(i)
# listNr2.sort()
# listNr2.reverse()
# print(listNr2)  
# # for i in str(listNr): 
# #   print(i,end=" ")

# # res = [int(x) for x in str(listNr)] 
# # print(str(res))
# listDif=[]
# for i in listNr:
#   if i not in listNr2:
#     listDif.append(i)
# print(listDif)  

# # __int__ these are magic methods

# #touples
# # nrArray = [1,2,3,4,5]
# nrTuples = (1,2,3,4,5) # cannot change the array
#                         #only count and index
# number = { "type":"int","value":23 }
# print(number["type"], end=" ")
# print(number["value"])
# number["value"] = 36
# # print(number["Value"]) -> results in error
# print(number.get("Type"),end=" ") # this won't
# print(number.get("value"),end=" ") 
# number.setdefault("isVisible",True)
# print(number["isVisible"])

# phnum = "075623238"
# translate = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
# translatedPhone=[]
# for i in phnum:
#   translatedPhone.append(translate[i])
#   # print(translate[i],end= " ")
# print(translatedPhone)

# emoji = {":)":"🙂",
#          ":(":"😞",
#          ":\\":"😕", 
        #  ":|":"😐",
#         }
# message = "hello there I was :( but now I'm :) ,tho sometimes I feel :\\ and :|"
# for i in message.split():
#   print(i,end=' ')
# print()
# emojified=[]
# for i in message.split():
#   emojified.append(emoji.get(i,i))

# for i in emojified:
#   print(i,end=' ')
# print()
# demoji=[]
# for word in emojified:
#   # print(word)
#   flag=False
#   for i in emoji.items():
#     if(i[1]==word):
#       flag=True
#       demoji.append(i[0])
#   if flag==False:
#     demoji.append(word)
      
# for i in demoji:
#   print(i,end=' ')
# print()   
    
# function

def woop():
  print("woop!")
  
woop()
# def woop():
#   print("Yo")
woop()

def woopi(word,n):
  for _ in range(n):
    print(str(word),end=" ")
  print()
woopi("hello",10)
woopi(3,10)

t1 = (1,2,3,4)
t2 = (1,2,4,3)
print(t1>t2)
dic={"a":"1","b":"2","c":"3"}
# dic.pop() 
print(dic)

def myfunc(stringus):
  for i in stringus:
    print(i,end=" ")
  print()
myfunc(t1)

def myfunc(stringus,stringus2):
  for i in stringus:
    print(i,end=" ")
  for i in stringus2:
    print(i,end=" ")
  print()  
myfunc(t1,t2)
myfunc(stringus2=t1,stringus=t2) #keyword argument!!!

try:
  print("It's okay")
except ValueError: 
  print("It's not okay")
except ZeroDivisionError:
  print("It's not okay, again...")

class MyFirstClass:
  def move(self):
    print(self)
  def draw(self):
    print("draw")
    
first_object = MyFirstClass()
first_object.draw()

pnt = MyFirstClass()
pnt.x = 10
pnt.y = 20
print(str(pnt.x)+" "+str(pnt.y))

class LED:
  def __init__(self,r,g,b):
    self.r=r
    self.g=g
    self.b=b
  def rgb(self):
    print(str(self.r)+" "+str(self.g)+" "+str(self.b))
    

led = LED(123,242,114)
led.r=23
led.rgb()

class Nothing:
  pass

class Object:
  def current_object(self):
    print("This is an object")
  def __init__(self):
    print("this is an object")
      

class Paint(Object):
  def __init__(self,color):
      self.color=color
      print(f"This paint is {color}")
      
p1 = Paint("blue")
p1.current_object()

obj1=Object()
p1=obj1

def max_number(array):
  maxi = array[0]
  for num in array:
    if num > maxi:
      maxi=num
  return maxi

print(max_number(t1))

class AnotherClass:
  def __init__(self):
    print("AnotherClass object created")
class YetAnotherClass(AnotherClass):
  def __init__(self):
      super().__init__()
      
ano = AnotherClass() 
ano2 = YetAnotherClass()

mypack.name.print_name("Dan")
name.print_name("Dan")
print_name("Dan")

print(random.random())
print(random.randint(1,50))

my_list = ["Dan","Danny","Dannio","Daniel","Don","Bogdan"]
print(random.choice(my_list))


class Dice:
  def roll(self):
      dice_numbers = (range(1,7))
      dice1 = random.choice(dice_numbers)
      dice2 = random.choice(dice_numbers)
      print(str(dice1)+" "+str(dice2))
  def roll(self):
      dice_numbers = (range(1,7))
      dice1 = random.choice(dice_numbers)
      dice2 = random.choice(dice_numbers)
      return dice1,dice2
    # When there's duplicates the last one applies


die1 = Dice()
print(die1.roll())

#FILES!!!

my_path = Path()
# print(my_path.exists()) 
# print(my_path.mkdir())
# print(my_path.rmdir())
# print(my_path.glob('*.py'))
for file in my_path.glob('*.py'):
  print(file)

