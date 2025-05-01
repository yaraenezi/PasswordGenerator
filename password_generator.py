# this program generates random passwords based on length
print('Want a new password?')
import random
import string

def getValidInput():
    while True:
        try:
            length = int(input('Enter desired length of password: '))
            # length is a positive integer
            if length <=0:
                print('Invalid input. Please enter a positive integer')
            else:
                return length
        except ValueError:
            print('Invalid input. Please enter a valid integer')

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

chars = list(letters + digits + punctuation)
weights = [3] * len(letters) + [2] * len(digits) + [1]* len(punctuation)
length = getValidInput()
password = ''.join(random.choices(chars, weights=weights, k=length))

print(f'Your random password is: {password}')