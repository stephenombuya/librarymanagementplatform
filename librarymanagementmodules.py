import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "library_management_system"
    )

mycursor = mydb.cursor()
# services that the teacher can perform function
def teacher_session():
            while 1:
                print("..........................")
                print("....LIBRARY SERVICES......")
                print("..........................")
                print(".    1.Borrow books      .")
                print(".    2. Return a book    .")
                print(".    3.log out           .")
                print("..........................")
                #among the choices the teacher should choose one in numerics
                insert_option = input(str("choose service: "))
                if insert_option == "1":
                    print("..................................CAUTION.....................................")
                    print("A book can  only be borrowed for a maximum of 10 days more than that,the book ")
                    print("______________________________________________________________________________")
                    print("will be counted overdue after 10 days and will be penalised upon returning")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    mycursor.execute("SELECT * FROM bookrecord; ")
                    for x in mycursor:
                        print(x)                    
                    book = input(("Enter book title: "))
                    Author = input(("Enter author: "))
                    Year = input(("Enter Year: "))
                    days = input(str("enter number of days: "))
                    query_values=(book,Author)
                    query_values1=(book,Author,Year,days)
                    # query to delete the borrowed book from the book records shelf
                    mycursor.execute("DELETE FROM bookRecord WHERE title = %s AND author = %s",query_values)
                    mydb.commit()  
                    if mycursor.rowcount < 1:
                        #if the book is not available in the records
                        print("the book is not available")
                    else:
                     #the borrowed book is recorded in the issued books table as an issued book
                     mycursor.execute("INSERT INTO issue (title,author,year,days) VALUES(%s,%s,%s,%s)",query_values1)         
                     mydb.commit()
                    if mycursor.rowcount < 1:
                            print("A book can  only be borrowed for a maximum of 10 days")
                    else:
                          print("Get the book at the front desk of the library")          
                elif insert_option == "2":
                    Tittle = input(str("Enter book title: "))
                    Author = input(str("Enter book Author name: "))
                    Year = input(str("Enter book year published: "))
                    School = input(str("Enter book department: "))
                    Genre = input(str("Enter book type: "))
                    query_values=(Tittle,Author,Year,School,Genre)
                    query_values1 = (Tittle,Author,Year)
                    #query to return the borrowed book to the book records
                    # query to remove the retrned book from the issued books
                    mycursor.execute("DELETE FROM issue WHERE title = %s AND author = %s AND year = %s",query_values1)         
                    mydb.commit() 
                    if mycursor.rowcount < 1:
                        print("______________________________________________________________________________________________________________________________")          
                        print("the book was either removed from the shelves due to overdue thus you have to  pay the penalty or confirm the details correctly")
                        print("______________________________________________________________________________________________________________________________")
                    else:
                     mycursor.execute("INSERT INTO bookRecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
                     mydb.commit()
                     print("book returned")    
                elif insert_option == "3":
                    break
                else:
                    print("invalid service") 
                    #services that can be accessed  the student function 
def student_session():
            while 1:
                print("..........................")
                print("....LIBRARY SERVICES......")
                print("..........................")
                print(".    1.Borrow books      .")
                print(".    2. Return a book    .")
                print(".    3.log out           .")
                print("..........................")
                insert_option = input(str("choose service: "))
                print("..........................")
                if insert_option == "1":
                    print("..................................CAUTION.....................................")
                    print("A book can  only be borrowed for a maximum of 10 days more than that,the book ")
                    print("______________________________________________________________________________")
                    print("will be counted overdue after 10 days and will be penalised upon returning")
                    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
                    mycursor.execute("SELECT * FROM bookrecord; ")
                    for x in mycursor:
                        print(x)
                    print("")
                    print("")
                    book = input(("Enter book title: "))
                    Author = input(("Enter author: "))
                    Year = input(("Enter Year: "))
                    days = input(str("enter number of days: "))
                    query_values=(book,Author)
                    query_values1=(book,Author,Year,days)
                    # query to delete the borrowed book from the book records shelf
                    mycursor.execute("DELETE FROM bookRecord WHERE title = %s AND author = %s",query_values)
                    mydb.commit()  
                    if mycursor.rowcount < 1:
                        #if the book is not available in the records
                        print("the book is not available")
                    else:
                     #the borrowed book is recorded in the issued books table as an issued book
                     mycursor.execute("INSERT INTO issue (title,author,year,days) VALUES(%s,%s,%s,%s)",query_values1)         
                     mydb.commit()
                    if mycursor.rowcount < 1:
                            print("A book can  only be borrowed for a maximum of 10 days")
                    else:
                          print("Get the book at the front desk of the library")   
                elif insert_option == "2":
                    print(".................................")
                    Tittle = input(str("Enter book title: "))
                    Author = input(str("Enter book Author name: "))
                    Year = input(str("Enter book year published: "))
                    School = input(str("Enter book department: "))
                    Genre = input(str("Enter book type: "))
                    query_values=(Tittle,Author,Year,School,Genre)
                    query_values1 = (Tittle,Author,Year)
                    #query to add the records of the returned book into the book records shelve
                    mycursor.execute("DELETE FROM issue WHERE title = %s AND author = %s AND year = %s",query_values1)         
                    mydb.commit() 
                    if mycursor.rowcount < 1:
                        print("______________________________________________________________________________________________________________________________")          
                        print("the book was either removed from the shelves due to overdue thus you have to  pay the penalty or confirm the details correctly")
                        print("______________________________________________________________________________________________________________________________")
                    else:
                     mycursor.execute("INSERT INTO bookRecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
                     mydb.commit()
                     print("book returned")  
                elif insert_option == "3":
                    break
                else:
                    print("invalid service")  
                    #an authetication function for the teacher if his/her password exists in the library database
def auth_teacher():
    print("...................................")
    print("login as a registered Teacher")
    print("'''''''''''''''''''''''''''''''''''")
    username = input(str("Enter Teacher username: "))
    password = input(str("enter Teacher password: "))
    query_value1 = (username,password)
    #query to confirm availabilty of password and username
    mycursor.execute("SELECT username FROM member WHERE username = %s and password = %s", query_value1)
    user_check = mycursor.fetchall()
    if user_check:
      teacher_session()
    else:
        print("invalid username or password kindly contact the library manager for assistance")
        print("....................................")
        print("register as teacher into the library")
        print("''''''''''''''''''''''''''''''''''''")

        username = input(str("teacher username: "))
        password = input(str("teacher password: "))
        query_values=(username,password)
        #query for self registration into the library system
        mycursor.execute("INSERT INTO member(username,password,privilege) VALUES(%s,%s,'teacher')",query_values)
        mydb.commit()
        print("-------------------------------------------------")
        print(" You have been registered succesfully! ")
        print("You can now log in")
        print("-------------------------------------------------")
     
#an authetication function for the teacher if his/her password exists in the library database
def auth_student():
    print("--------------------------------------")
    print("login as a registered student")
    print("--------------------------------------")
    username = input(str("Enter student username: "))
    password = input(str("enter student password: "))
    query_value1 = (username,password)
    #query to confirm availabilty of password and username
    mycursor.execute("SELECT username FROM member WHERE username = %s and password = %s", query_value1)
    user_check = mycursor.fetchall()
    if user_check:
      student_session()
    else:
        print("invalid username or password kindly contact the library manager for assistance or sign up")
        
        print("--------------------------------")
        print("register into the library")
        print("................................")
        username = input(str("student username: "))
        password = input(str("student password: "))
        query_values=(username,password)
     #query for self registration into the library system
        mycursor.execute("INSERT INTO member(username,password,privilege) VALUES(%s,%s,'student')",query_values)
        mydb.commit()
        print("-------------------------------------------------")
        print(" You have been registered succesfully! ")
        print("You can now log in")
        print("-------------------------------------------------")
#a function for the servisec that can be accessed by the admin
def admin_session():
    while 1:
        print("admin menu")
        print("----------")
        print("1. register new student")
        print("2. register new teacher")
        print("3. deregister existing student")
        print("4. deregister existing student")
        print("5. add books delivered")
        print("6. remove unreturned and overdue books from issued books records")
        print("7. log out")
        user_option = input(str("option: "))
        if user_option == "1":
            print("")
            print("register new student into the library")
            username = input(str("student username: "))
            password = input(str("student password: "))
            query_values=(username,password)
            #query to add a student to the library system
            mycursor.execute("INSERT INTO member(username,password,privilege) VALUES(%s,%s,'student')",query_values)
            mydb.commit()
            print("--------------------------------------")
            print(username +" has been registered as a student")
        elif user_option == "2":
            print("")
            print("register new Teacher int the library")
            username = input(str("Teacher username: "))
            password = input(str("Teacher password: "))
            query_values=(username,password)
           
            #query to add a student to the library system
            mycursor.execute("INSERT INTO member(username,password,privilege) VALUES(%s,%s,'Teacher')",query_values)
            mydb.commit()
            print("--------------------------------------")
            print(username +" has been registered as a teacher")
        elif user_option =="3":
            print("")
            print("Diregister existing student")
            username = input(str("Student username: "))
            query_values = (username,"student")
            #query to remove a student from the library system
            mycursor.execute("DELETE FROM member WHERE username = %s AND privilege = %s",query_values)
            mydb.commit()
            print("--------------------------------------")
            if mycursor.rowcount < 1:
                print("user does notexist")
            else:
                print(username + " has been diregistered")
        elif user_option =="4":
            print("")
            print("Diregister existing teacher")
            username = input(str("teacher username: "))
            query_values = (username,"teacher")
                        
            #query to remove a student from the library system
            mycursor.execute("DELETE FROM member WHERE username = %s AND privilege = %s",query_values)
            mydb.commit()
            print("--------------------------------------")            
            if mycursor.rowcount < 1:
                print("user does notexist")
            else:
                print(username + " has been diregistered")
        elif user_option =="5":
            print("")
            print("Add the delivered book")
            Tittle = input(str("Enter book tittle: "))
            Author = input(str("Enter book Author name: "))
            Year = input(str("Enter book year published: "))
            School = input(str("Enter book department: "))
            Genre = input(str("Enter book type: "))
            query_values=(Tittle,Author,Year,School,Genre)
            #query to add a book to the book Records
            mycursor.execute("INSERT INTO bookRecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
            mydb.commit()
            print("-------------------------------------------")
            if mycursor.rowcount < 1:
                print("The book record has not been added")
            else:
                print(Tittle + " By " + Author + " has been Recorded")
                print("----------------------------------------")

        elif user_option == "6":
            print("")  
            print("remove unreturned and are overdue books from issued book records ") 
            #Title = input(str("Enter book tittle: "))
            #Genre = input(str("Enter book genre: "))
            #days = input(str("Enter days of overdue: "))
            #query_values = (Tittle,Genre)
            #query_values = (days)
            #query to remove unexisting book from the shelves when displaced
            mycursor.execute("DELETE FROM issue WHERE days > 10")
            mydb.commit()
            print("------------------------------------------")
            if mycursor.rowcount < 1:
                print("The book does not exist in the records")
            else:
                print("Overdue books have been removed from the book records")
                print("-------------------------------------------")

        elif user_option == "7":
            break
        else:
            print("invalid option")
# an authentication function for the admin
def auth_manager():
    print(".................")
    print(". manager login .")
    print(".................")
    username = input(str("username: "))
    password = input(str("password: "))
    if username == "Admin":
        if password == "password":
            admin_session()
        else:
            print("incorrect password")
    else:
        print("login detals incorrect")
    

def main():
    while 1:
       print("-----------------------------------------------")
       print("WELCOME TO THE LIBRARY")
       print("-----------------------------------------------")
       print("LOGIN AS")
       print("..........................")
       print(".  1 $ STUDENT           .")
       print(".  2 $ TEACHER           .")
       print(".  3 $ LIBRARY MANAGER   .")
       print(".  4 $ LOG OUT           .")
       print("..........................")
       insert_choice = input(str("enter your choice: "))
  
       if insert_choice == "1":
#calling the function for student auntication
          auth_student()
       elif insert_choice == "2":
 #calling the function for teacher auntication
          auth_teacher()
       elif insert_choice =="3":
#calling the function for library manager auntication
           auth_manager()
       elif insert_choice == "4":
           break
       else:
             print("invalid choice")

main()
   

