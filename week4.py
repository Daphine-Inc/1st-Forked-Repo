class person:
    def __init__ (self, name, age, gender):
        self.name= name
        self.age= age
        self.gender= gender

    def introduce (self):
        print(f"Hi, my name is {self.name} and I am a {self.age} years old {self.gender}")
        
p1 = person("Joy", 34, "female")
p1.introduce()

