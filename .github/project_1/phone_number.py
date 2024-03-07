import re
import time


def phone_number() :
   ppp = r'^([+][4][9])\d{1,10}$'
   
   while True :
      phonenumber = input('write a valid German phone number :')
      result =  re.search(ppp, phonenumber)

      if result :
         anonymos = phonenumber[:-5]+'****'
         print('Valid phone number !',anonymos)
         return phonenumber
    
      elif result is None : 
        print('Invalid phone number, Please enter a valid German phone number.')   
        print('Should start with "+49" followed by 1 to 10 digits.')
      return phone_number()

phone_number()
