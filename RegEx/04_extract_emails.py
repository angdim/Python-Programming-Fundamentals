import re
text = input()
template = r'(\s[a-z]+)[\._-]?[a-z]+@[a-z-]+(.[a-z-]+)?\.[a-z]+(?=/.)?'
mail_list = re.finditer(template, text)
for mail in mail_list:
    print(mail.group())
