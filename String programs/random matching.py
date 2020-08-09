import string
import random

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

t = "geek"

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(t)))
attemptNext = ''

completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    for i in range(len(t)):
        if attemptThis[i] == t[i]:
            attemptNext += t[i]
        else:
            completed = False
            attemptNext += random.choice(possibleCharacters)

    attemptThis = attemptNext
