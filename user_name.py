import re
import time


def user_name() : 
  p = r'^\S\w{1,10}$'
  while True :
      b = input("Type your username :")
      result = re.search(p, b)
      if result is not None :
        print('Username is valid')
        return b
      elif result is None :
         print('Please entrer a valid username and Try again')
      return user_name() 

