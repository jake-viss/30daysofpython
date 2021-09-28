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

python_acronym = "PFE"
coding_acronym = "CFA"

print(coding_acronym.find("C"))
print(coding_acronym.find("F"))
company="Coding for all People"
print(company.rfind("l"))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
print(sentence.rindex("because"))
because_3 = sentence[31:54]
print(because_3)
print(sentence.find("because"))

company="Coding For All"
print(company.startswith("Coding"))
print(company.endswith("coding"))
company = "  Coding For All  "
print(company.strip("  "))

library_list = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("# ".join(library_list))

print("I am enjoying this challenge. \nI just wonder what is next.")

print("Name\tAge\tCountry\tCity \nAsabeneh\t250\tFindland\tHelsinki")


radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)

print("""
8 + 6 = 14
8 - 6 =2""")
