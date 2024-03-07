import re
import time



def password_validation() :
  pp = r'.*\d.*[A-Z].*[a-z]\W*.{6,20}'

  while True :
        password = input('write a valid password :')  
        result = re.search(pp, password) 

        if result is not None :
          print('password is valid ')
          return password
          
        elif result is None :
          print('\nplease enter a valid password')
          print('Should have at least one number.')
          print('Should have at least one uppercase and one lowercase character.')
          print('Should have at least one special symbol.')
          print('Should be between 6 to 20 characters long.\n')
        return password_validation()
  
