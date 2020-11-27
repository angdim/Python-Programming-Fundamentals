import re
sentence = input().lower()
word = input().lower()
template = r'\b(' + word + r')\b'
count = re.findall(template, sentence)
print(len(count))
