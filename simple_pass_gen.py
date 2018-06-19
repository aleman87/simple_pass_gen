import random
import string
import sys

password = []
for i in range(int(sys.argv[1])):
    if(i ==0):
        password.append(random.choice(string.letters))
    else:
        num_or_char = random.randint(0,2)
        if(num_or_char == 0):
            #it is a number we want
            password.append(random.randint(0,9))
        elif( num_or_char ==1):
            #generate a letter (either cap or lower case)
            password.append(random.choice(string.letters))
        else:
            #generate a random punctuation
            password.append(random.choice(string.punctuation))

pass_string = ''.join(str(e) for e in password)
print(pass_string)