import re
txt = input()
word = re.findall(r'\b[A-Z][a-z]{3,}\b', txt)
print(word)
