print("Welcome to Jerrys Sandwich Shop")

sandwich =['tuna','turkey','chicken']
bread = ['wheat', 'rye', 'pumpernickel']
toppings=['onion', 'lettuce','mustard','sweetonion salad_dressing', 'tomatoes']

if "tuna" in sandwich:
    print("What type of bread would you like? ")

    if "wheat" in bread:
        print('What type of topping would you like ')

else:
    print("we only have the breads listed ")

if "turkey" in sandwich:
    print("It would taste great on rye or pumpernickel ")

else:
    print("We have the perfect bread for that ")

if "chicken" in sandwich:
    print("Add all of the toppings ")

else:
    print("We are solde out! ")

print("Thanks for coming to Jerry's ")
