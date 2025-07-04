import sqlite3
from contextlib import contextmanager

#Constante que indica o caminho para o diretorio para o banco de dados
DB_NAME = "C:\\Users\\Fraiburgo\\Desktop\\tedste\\studentRegistrationSQL\\student.db"
def undo(msg:str, e, conexao):
    conexao.rollback()
    raise

@contextmanager   
def get_cursor():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    try:
        yield cursor
        conexao.commit()


    except sqlite3.IntegrityError as e:
        undo(f"Ocorreu o erro", e, conexao)


    except sqlite3.ProgrammingError as e:
        undo(f"Ocorreu o erro", e, conexao)
   
    except sqlite3.OperationalError as e:
        undo(f"Ocorreu o erro", e, conexao)
   
    except sqlite3.DatabaseError as e:
        undo(f"Ocorreu o erro", e, conexao)
       
   
    except Exception as e:
            undo(f"Ocorreu o erro", e, conexao)
   
    finally:
        conexao.close()

def create_table():
    with get_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                idade INTEGER
            )
        """)