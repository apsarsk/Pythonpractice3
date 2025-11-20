import re
# import re as re
# text = "The amount is 1500 and not 0"
# patten=r"\d+"
# fin=re.findall(patten,text)
# print(fin)

# '*'
# text = "Ms. Smith and Mr. Jones"
# patten=r"M(s|r|rs)\.\s *Jones"
# fin=re.search(patten,text)
# print(fin.group())

# "?"
# text = "The color is blue and the colour is red."
# match=r"colou?r"
# print(re.findall(match,text))

# {n}
# text = "Call 555-1234 or 9991234."
# pattern = r'\d{3}'
# print(re.findall(pattern,text))

# text = "The IP is 192.168.1.1 and not 5.0.0.999"
# pattern=r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# print(re.search(pattern,text).group())

# text = "This is <b>first</b> and <b>second</b>."
# match=r'<b>.*?</b>'
# l_matches=re.findall(match,text)
# print(l_matches)

# text = "ID: PRD12345, Old ID: ABC001, Short: X12"
# pattern=r'\b\w{5,8}\b'
# print(re.findall(pattern,text))

# emails = [
#     "user123@domain.com",
#     "short@test.com",
#     "superlongusername2025@server.net"
# ]

# pattern=r'^[a-z]{3,20}@'
#
# for email in emails:
#     match= re.search(pattern,email)
#     result= 'Match' if match else 'Not Match'
#     print(f"Email: {email.ljust(30)} -> {result}")

# text='today date is :19/11/2025'
# pattern=r"\d{2}/\d{2}/\d{4}"
# print(re.findall(pattern,text))

# text = 'date1: 19/11/2025, date2: 19-11-2025'
# pattern= r'\d{2}[-/.]\d{2}[-/.]\d{4}'
# print(re.findall(pattern, text))

