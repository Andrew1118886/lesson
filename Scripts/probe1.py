from pprint import pprint
word ='Hello'
rainbow = ['red', 'green', 'blue']
primes = [2, 3, 5, 7, 11, 13]

chars = list(word)

text = word*2
print(text)
rainbow.extend(['violet','yellow']) #список - это изменяемый объект



primes.insert(4, 1)
print(primes*-1)