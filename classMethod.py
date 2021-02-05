#proper way to create a class and object

class Parrot:

    #define attributes
    species = 'bird'

    #instance_attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self,song):
        return '{} sings {} '.format(self.name,song)
#instantiate the parrot class
blu = Parrot('Blu',10)
woo = Parrot('woo',15)

#access the class attributes
print('Blu is a {}'.format(blu.species))
print('woo is a {}'.format(woo.species))

#access the instance attributes
print('{} is {} years old '.format(blu.name, blu.age))
print('{} is {} years old '.format(woo.name, woo.age))

#access the methods
print(blu.sing('Happy'))