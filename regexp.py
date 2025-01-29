import re

email_data="Nithinkumar <nithinkkumar@gmail.com>, Charitha<cherrydhruva48@gmail.com>"

result= re.search(r"Nithin", email_data)
print(result)

result= re.findall(r"Nit", email_data)
print(result)

result= re.search(r"Nit[o,m]", email_data)
print(result)

result= re.search(r"Nit[a-z]", email_data)
print(result)

result= re.search(r"Nit[a-z]{2}", email_data)
print(result)

result= re.search(r"Nit[a-z]+", email_data)
print(result)


result= re.search(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)


result= re.findall(r"[A-Za-z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)


result=re.search(r"[a-zA-Z0-9_@.]+", email_data)
print(result)
