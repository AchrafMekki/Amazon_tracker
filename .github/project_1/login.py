import re
import time


def login () : 
   attempts = 3
   registered_users = {}

   for x in range(attempts) :
      print (x)
      user_name  = input("Enter username : ")
      pass_word = input("Enter password :")
      
      if user_name  in registered_users and registered_users[user_name] == pass_word:
        print(' Login is successful')
        return user_name
      else :
        print('Invalid username or password. Please try again.')
        
   print("You have used all login attempts. Try again after 5 seconds.")
   time.sleep(5)
   return login()



   