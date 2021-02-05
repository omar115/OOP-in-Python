class Bird:

    def __init__(self):
        print('Bird  is ready')
    
    def whoIsThis(self):
        print('Bird')
    
    def swim(self):
        print('swim faster')

#child class
class Penguin(Bird):
    
    def __init__(self):
        super().__init__()      #call super function, super function call the init function of parent class
        print('Penguin is ready')
    
    def whoIsThis(self):
        print('Penguin')
    
    def run(self):
        print('faster')
    
peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()