import re
import time



def register() : 

  registered_users = {}
  i = input('username :')

  while i in registered_users : 
    print('Username already exist. Please choose another one ')
    #i = input('username :')    
    return i  
  
  p = input('Enter password : ')
  registered_users.update({i: p}) #key : value
  
  print(f'{i} You successfully Registered !')
  print('Updated registered_users:', registered_users)

    
  


