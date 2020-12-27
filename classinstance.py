class Employee: #class
    
    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Omar','Hasan', 25000)
emp_2 = Employee('Mazhar','Hossain',35000)

print(emp_1)
print(emp_2)

print('The first name of employee 1 is ',emp_1.first)
print('The email of employee 1 is ', emp_1.email)

print('The employee full name is ',emp_1.fullname())



