import random
import pyperclip

rand = random.randint(1,10)
print(rand)

pyperclip.copy('Hello World!')
print(pyperclip.paste())