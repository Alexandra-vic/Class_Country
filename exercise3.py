class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, numb):
        self.numb = numb

    def __str__(self):
        return f'Через {self.numb} лет, {self.name} исполнится {self.age + self.numb} лет'    
                   
p = Person('John', 20, 'male')
print(f'{p.name}, {p.age}, {p.gender}')

p.calculate_age(10)
print(p)
        