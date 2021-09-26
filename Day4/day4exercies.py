# 1 through 17
a, b, c, d = "Thirty", "Days", "Of", "Python"
combined = a + " "+ b + " " + c + " " + d
e, f, g = "Coding ", "for ", "All"
combined2 = e, f, g

company = "Coding For All"
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
print(company[0:6])
print(company.find("All"))
print(company.replace("Coding","Python"))
company2 = company.replace("Coding", "Python")
print(company2.replace("All","Everyone"))
print(company.split(" "))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
list_companies = companies.split(",")
print(list_companies[1])

print(company[10])