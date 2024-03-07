import re
import time


def what_to_do_first(x) :
    if x == '1' :
      return 'Here you can Register'      
    elif x == '0' :
      return  '!!* Welcome Back *!!'
    else :
       return 'Invalid input'
    
a = input("---> 'Enter '1' to Register  --->  OR  --->  Enter '0' to Login : ") 
print(what_to_do_first(a))