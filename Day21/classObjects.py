class Person:
    def __init__(self, firstname='None', lastname='None', age='N/A', country='N/A', city='N/A'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person('Jake', 'Vissering', 31, 'USA', 'Seattle')
p2 = Person()


class Student(Person):
    def __init__(self, firstname='None', lastname='None', age='N/A', country='N/A', city='N/A', gender='N/A'):
        super().__init__(firstname, lastname, age, country, city)
        self.gender = gender

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s1 = Student('Jen', 'Kisaki', 36, 'USA', 'Washington D.C.', 'female')
s2 = Student('Boomer', 'Saison', 56, 'USA', 'Nashville', 'male')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
