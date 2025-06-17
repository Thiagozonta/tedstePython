import dao.student_dao as dao
from models.student import Student

def create_record(name, email, age):
    if age >= 130:
        print("Erro: idade incorreta")
        return

    student = Student(name, email, age)
    dao.insert_student(student)
    
    if age < 10:
        print("aceitamos matriculas apenas para alunos maiores de idade")
        return
    dao.insert_Student(student)