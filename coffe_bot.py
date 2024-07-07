#Imports Functions from utils.py script
from utils import print_message, get_size, order_latte

#Defines coffe_bot Function
def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = 'y'
  drinks = []
#Collects Drink orders, and keeps track of Drinks
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))
    drinks.append(drink)

    while True:
      order_drink = input("Would you like to order another drink? (y/n) ")
      if order_drink == 'y' or 'n':
        break
  
#Prints out drinks from drink list 
  print("Okay, so I have: ")   
  for drink in drinks:
    print("-", drink)   
#Takes users name to issue a response 
  name = input('Can I get your name please? \n> ')
  print('Thanks, {}! Your order will be ready shortly.'.format(name))

#Gets the Users Drink type/ Brewed coffe/ Mocha/Latte
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
#prompts User to order special limited edition mocha coffe
def order_mocha():
  while True: 
    res = input("Would you like to try our limited-edition peppermint mocha? \n [a] Sure! \n [b] Maybe next time!")
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'   
    print_message()


#Calls the coffe function when user runs script.py    
coffee_bot()
