import sqlite3
conn = sqlite3.connect("todopy.sqlite")
c = conn.cursor()

class ToDos:

    def create_todo(self, arg):
        c.execute("""
        INSERT INTO todos (todo)
        VALUES(?)""", (arg, )
        )

    def get_list(self):
        c.execute("""
        SELECT * FROM todos
        ORDER BY todo_id
        """)

    def delete_todo(self, arg):
        c.execute("""
        DELETE FROM todos
        WHERE todo = ? """, (arg, ))

    def search_todo(self, arg):
        c.execute("""
        SELECT * FROM todos
        WHERE todo = ?""", (arg, ))

def print_menu():
    cons = input("""Choose the option:
    1. Create new a todo
    2. List all existing todos
    3. Delete todos
    4. Search todos
    """)
todosObj = ToDos()

while True:
    print_menu()
    resp = int(input())
    if resp == 1:
        print("Create new a todo")
        inpNewToDo = str(input("Input of a new todo"))
        todosObj.create_todo(inpNewToDo)

    elif resp == 2:
        print("List all existing todos")
        todosObj.get_list()
        all_records = c.fetchall()
        for record in all_records:
            print(record)

    elif resp == 3:
        print("Delete todos")
        deletingItem = str(input("Input of deleting item in a list"))
        todosObj.delete_todo(deletingItem)
    elif resp == 4:
        print("Search todos")
        searchedEl = str(input("What are you looking for?"))
        todosObj.search_todo(searchedEl)
        print(c.fetchall())

    else:
        print("Thank for using app")
        break

conn.commit()
conn.close()