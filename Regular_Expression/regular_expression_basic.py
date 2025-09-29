import re

text = "My phone number is 123-456-7890 and email is test@example.com"

# 1. Find all digits
digits = re.findall(r'\d+', text)
print(digits)  # ['123', '456', '7890']

# 2. Find phone number pattern
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())  # 123-456-7890

# 3. Find email
email = re.search(r'\w+@\w+\.\w+', text)
print(email.group())  # test@example.com

# 4. Replace digits with *
masked = re.sub(r'\d', '*', text)
print(masked)  # My phone number is ***-***-**** and email is test@example.com

# 5. Split text by spaces
words = re.split(r'\s', text)
print(words)  # ['My', 'phone', 'number', 'is', '123-456-7890', 'and', 'email', 'is', 'test@example.com']
