import mysql.connector
from datetime import date, timedelta

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="library_management_system"
)

# Create a cursor object
mycursor = mydb.cursor()

# Function to display the main menu
def display_menu():
    print("\nLibrary Management System")
    print("1. Book Management")
    print("2. Issue Management")
    print("3. Member Management")
    print("4. Exit")

# Function to manage books
def book_management():
    print("\nBook Management")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. View Books")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        update_book()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        view_books()
    else:
        print("Invalid choice")

# Function to add a book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter book year: ")
    school = input("Enter your school: ")
    book_type = input("Enter book type: ")
    sql = "INSERT INTO bookrecord (title, author, year, school, type) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author, year, school, book_type)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Book added successfully")

# Function to update a book
def update_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter new book title: ")
    author = input("Enter new author name: ")
    category = input("Enter new book category: ")
    sql = "UPDATE bookRecord SET title = %s, author = %s, category = %s WHERE Bno = %s"
    values = (title, author, category, book_id)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Book updated successfully")

# Function to delete a book
def delete_book():
    book_id = int(input("Enter book ID: "))
    sql = "DELETE FROM bookRecord WHERE Bno = %s"
    value = (book_id,)
    mycursor.execute(sql, value)
    mydb.commit()
    print("Book deleted successfully")

# Function to view all books
def view_books():
    sql = "SELECT * FROM bookRecord"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("\nBooks:")
    for row in result:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Category: {row[3]}")

# Function to manage issues
def issue_management():
    print("\nIssue Management")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. View Issued Books")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        issue_book()
    elif choice == 2:
        return_book()
    elif choice == 3:
        view_issued_books()
    else:
        print("Invalid choice")

# Function to issue a book
def issue_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))
    issue_date = date.today()
    due_date = issue_date + timedelta(days=10)
    sql = "INSERT INTO issue (Bno, Mno, issue_date, due_date) VALUES (%s, %s, %s, %s)"
    values = (book_id, member_id, issue_date, due_date)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Book issued successfully")

# Function to return a book
def return_book():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))
    sql = "DELETE FROM issue WHERE Bno = %s AND Mno = %s"
    values = (book_id, member_id)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Book returned successfully")

# Function to view issued books
def view_issued_books():
    sql = "SELECT b.title, m.name, i.issue_date, i.due_date FROM issue i JOIN bookRecord b ON i.Bno = b.Bno JOIN member m ON i.Mno = m.Mno"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("\nIssued Books:")
    for row in result:
        print(f"Title: {row[0]}, Member: {row[1]}, Issue Date: {row[2]}, Due Date: {row[3]}")

# Function to manage members
def member_management():
    print("\nMember Management")
    print("1. Add Member")
    print("2. Update Member")
    print("3. Delete Member")
    print("4. View Members")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_member()
    elif choice == 2:
        update_member()
    elif choice == 3:
        delete_member()
    elif choice == 4:
        view_members()
    else:
        print("Invalid choice")

# Function to add a member
def add_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    phone = input("Enter member phone number: ")
    sql = "INSERT INTO member (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Member added successfully")

# Function to update a member
def update_member():
    member_id = int(input("Enter member ID: "))
    name = input("Enter new member name: ")
    email = input("Enter new member email: ")
    phone = input("Enter new member phone number: ")
    sql = "UPDATE member SET name = %s, email = %s, phone = %s WHERE Mno = %s"
    values = (name, email, phone, member_id)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Member updated successfully")

# Function to delete a member
def delete_member():
    member_id = int(input("Enter member ID: "))
    sql = "DELETE FROM member WHERE Mno = %s"
    value = (member_id,)
    mycursor.execute(sql, value)
    mydb.commit()
    print("Member deleted successfully")

# Function to view all members
def view_members():
    sql = "SELECT * FROM member"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("\nMembers:")
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")

# Main program loop
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_management()
    elif choice == 2:
        issue_management()
    elif choice == 3:
        member_management()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
