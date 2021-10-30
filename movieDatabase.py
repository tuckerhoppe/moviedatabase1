import sqlite3

connection = sqlite3.connect('movies2.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (name TEXT, fav1 TEXT, fav2 TEXT, fav3 TEXT)")

def addPerson(name, fav1, fav2, fav3):
    values = (name,fav1, fav2, fav3)
    cursor.execute("INSERT INTO movies VALUES (?,?,?,?)", values)
    connection.commit()


name = "Harold"
fav1 = "interstellar"
fav2 = "inception"
fav3 = "cars"
values = (name,fav1, fav2, fav3)
cursor.execute("INSERT INTO movies VALUES (?,?,?,?)", values)
connection.commit()

addPerson('Tom', 'star wars', 'napoleon dynamyte', 'Tom and Jerry')
addPerson('Jack', 'Harry Potter', 'Star wars', 'Inception')

print('hey sql!')

choice = None
while choice != "5":
    print("1) Display List")
    print("2) Add Person")
    print("3) Edit Person's Movie")
    print("4) Delete Person")
    print("5) List a persons favorite movies")
    print("6) Quit")
    choice = input("> ")
    print()

    if choice == "1":
        # Display List
        cursor.execute("SELECT * FROM movies")
        
        print("{:<25}  {:<25}  {:<25}  {:<25}".format("Name", "Favorite 1", "Favorite 2", "Favorite 3"))
        print("=" *150)
        for record in cursor.fetchall():
            print("{:<25}  {:<25}  {:<25} {:<25}".format(record[0], record[1],
                                                  record[2], record[3]))

    elif choice == "2":
        # Add Person's Fav's
        try:
            name = input("Name: ")
            fav1 = input("Favorite 1: ")
            fav2 = input("Favorite 2: ")
            fav3 = input("Favorite 3: ")
            addPerson(name,fav1, fav2, fav3)
        except ValueError:
            print("Invalid Entry!")

    elif choice == "3":
        # Update Favorites
        try:
            name = input("Name: ")
            fav1 = (input("Favorite 1: "))
            values = (fav1, name)  # Make sure order is correct
            cursor.execute("UPDATE movies SET fav1 = ? WHERE name = ?",
                           values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid name!")
        except ValueError:
            print("Invalid pay!")

    elif choice == "4":
        # Delete employee
        name = input("Name: ")
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM movies WHERE name = ?", values)
        connection.commit()
    
    elif choice == "5":
        # Delete employee
        name = input("Name: ")
        if name == None:
            continue
        values = (name, )
        cursor.execute("SELECT * FROM movies WHERE name = ?", values)
        record = cursor.fetchall()
        print("{:<25}  {:<25}  {:<25} {:<25}".format('record[0]', "hey", "hey", "hey"))
    print()

# Close the database connection before exiting
connection.close()
