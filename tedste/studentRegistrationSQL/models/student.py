class Student:

        #metodo construtor da classe Aluno/Student 
    def __init__(self, name, email, age, id=None):

        self.id = id
        self.name = name
        self.email = email
        self.age = age

def __repr__(self):
     return f"student(id={self.id}), Name = {self.name}, email = {self.email}, age{self.age}"