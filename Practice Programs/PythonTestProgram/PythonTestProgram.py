import sys

sys.path.append(r'D:\Alex\Documents\Python Programs\Practice Programs\Phone')
#print(sys.path)

import G3
G3.G3()

from Import_File import std_power_of_num

n = std_power_of_num(2)
print(n)
#age = int(input("Enter your age: "))
#print("your age is", age)

#if(age <= 23):
 #   print("Hello fellow zoomer")
#elif age >= 30:
 #   print("Hello boomer")
#else:
 #  print("Hello cringe millenial")


#words = ['zoomer', 'boomer', 'doomer', 'coomer']
#for w in words:
  #  print(w)

#for n in range(len(words)):
  #  print(n, words[n])

#print(sum(range(0, 4)))
#print(list(range(0,4)))


#def pass_funct(n):
 #   pass #used as place-holder in empty function because something needs to be written in a function



#def pos_print(arg, /): #positional only arguement (only value inputted)
 #   print(arg)

#def kwd_print(*, arg):
   # """Documentation string

#yeah boyyyyyyyyy"""
#    print(arg)

#def both_print(arg1, /, arg2, *, arg3): #arg2 can be postional or keyword
 #   print(arg1 + arg2 + arg3)

#num = pos_print(1)
#num2 = kwd_print(arg=2)
#num3 = both_print(1, 2, arg3=3)
#print(kwd_print.__doc__)

#fruits = ['apples', 'oranges', 'bannanas', 'pear', 'kiwi', 'apple', 'pear']
#fruits.append('kiwi')
#print(fruits)

#list1 = ['physics', 'math,', 'chemistry']
#list2 = list(range(5))
#list1.extend(list2)
#print(list1)
#list1.insert(3, "biology")
#print(list1)
#list1.pop()

#def doubler(n):
 #   return lambda a: a * n

#double = doubler(2)
#print(double(11))
#print(double(3))