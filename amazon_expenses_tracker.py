import re

print('\n\n#### Welcome to our new Amazon Tracker #####\n\n')

print ('******* Choose to Sign-in or to Register ********\n\n')



def what_to_do_first(x) :
    if x == '1' :
      return 'Here you can Register'      
    elif x == '0' :
      return  '!!* Welcome Back *!!'
    else :
       return 'Invalid input'
    
a = input("---> 'Enter '1' to Register  --->  OR  --->  Enter '0' to Login : ") 
print(what_to_do_first(a))


def user_name() : 
  p = r'^\S\w{1,10}$'
  while True :
      b = input("Type your username :")
      result = re.search(p, b)
      if result is not None :
        print('Username is valid')
        return b
      elif result == None :
         print('Please entrer a valid username and Try again')
  



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


print(user_name())


validated_password = password_validation()
print('Validated Password:', validated_password)

print(phone_number())
print(what_to_do_first())


def login (username,password,x ) : 
   attempts = 3 
   user_name  = input("Enter username : ")
   pass_word = input("Enter password :")
   for x in range(attempts) :
      input