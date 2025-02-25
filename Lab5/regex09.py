import re
txt = input()
word = r'(?<!^)(?=[A-Z])'
result = re.sub(word , ' ', txt)
print(result)