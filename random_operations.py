import random

#get the random value from 0 to 1. 0 is inclusive and 1 is exclusive
value = random.random()
print(value)

#get the random value around the given range
value1 = random.uniform(2, 37)
print(value1)

#Get the random integer around the given range
value2 =  random.randint(2, 35)

print(value2)

vegetables = ["carrot", "Brinjal", "onion", "Tomato"]

#picking the choice randomly from the list
random_vegetable = random.choice(vegetables)

print(random_vegetable)

#Creating list of numbers from 1 to 52
deck = list(range(1, 53))

# print(deck)

#shuffle the list
random.shuffle(deck)

print(deck)

#Taking the sample of k unique values randomly
handover = random.sample(deck, k=5)
print(handover)

print(help(random))



