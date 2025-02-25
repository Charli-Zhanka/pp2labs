import re  
txt = input()
word = re.findall(r'\b^a.*b$\b', txt)
print(word)