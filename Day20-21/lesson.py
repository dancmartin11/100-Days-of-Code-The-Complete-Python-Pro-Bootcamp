#Class Inheritance
'''
Classes can inherit:
    - Attributes
    - Methods

We put the parent class inside the parenthesis when we create the child class (e.j. class ChildClass(ParentClass): )
We use the super() init method inside the __init__ to get attributes from a super class (inherit from another class)
'''

class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale.")
  
#Create Fish class inheriting from the Animal class      
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print("Moving in water.")
        
    #Create the breathe function for Fish (inheriting from Animal, but modifying it)
    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

#Create an instance of the class and test methods and attributes
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)