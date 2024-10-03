import pymysql
from pymysql import MySQLError
from datetime import date

def create_connection():
    try:
        connection = pymysql.connect(
            host='localhost',       
            database='Library_management_system',  
            user='root',            
            password='pE25+tERNjuku',
            port= 3306
        )
        print("Connection with MySQL is successful")
        return connection
    except MySQLError as e:
        print("Error encountered when connecting with MySQL", e)
        return None
    
def add_book(connection, title, author, genre, publisher, publication_date, isbn, num_copies, shelf_location, language_, edition, pages):
    try:
        with connection.cursor() as cursor:
            insert_query = """insert into books(title, author, genre, publisher, publication_date, isbn, num_copies, shelf_location, language_, edition, pages) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            book_data = (title, author, genre, publisher, publication_date, isbn, num_copies, shelf_location, language_, edition, pages)
            cursor.execute(insert_query, book_data)
        connection.commit()
        print("Book added successfully")
        
    except MySQLError as e:
        print("Failed to add book", e) 
        
def add_member(connection, first_name,last_name,date_of_birth,address,phone_number,email,membership_type,membership_start_date,membership_expiry_date,membership_status,outstanding_fees,num_books_borrowed, identification_document):
    try:
        with connection.cursor() as cursor:
            insert_query = """INSERT INTO members (first_name, last_name, date_of_birth, address, phone_number, email, membership_type, 
                                                   membership_start_date, membership_expiry_date, membership_status, 
                                                   outstanding_fees, num_books_borrowed, identification_document) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            member_data = (first_name, last_name, date_of_birth, address, phone_number, email, membership_type, 
                           membership_start_date, membership_expiry_date, membership_status, outstanding_fees, 
                           num_books_borrowed, identification_document)
            cursor.execute(insert_query, member_data)
        connection.commit()
        print("New member added successfully")            
        
    except MySQLError as e:
        print("Error encountered when adding new member", e)
        
def add_transaction(connection, member_id, book_id,transaction_type, ):
    try:
        with connection.cursor as cursor:
            pass
    
    except MySQLError as e:
        pass


def main():
    connection = create_connection()
    
    while True:
        print("\nLibrary MAnagement System")
        print("1. Add a book")
        print("2. Add a new member")
        print("3. Exit")
        choice = input("Enter your choice:  ")
        
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            publisher = input("Enter publisher: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            isbn = input("Enter ISBN: ")
            num_copies = int(input("Enter number of copies: "))
            shelf_location = input("Enter shelf location: ")
            language_ = input("Enter language: ")
            edition = input("Enter edition: ")
            pages = int(input("Enter number of pages: "))
            
            add_book(connection, title, author, genre, publisher, publication_date, isbn, num_copies, shelf_location, language_, edition, pages)
        
        elif choice == "2":
            first_name = input("Enter first name:  ")
            last_name = input("Enter last name:  ")
            date_of_birth = input("Enter date of birth:  ")
            address = input("Enter address:  ")
            phone_number = int(input("Enter phone number:  "))
            email = input("Enter email address:  ")
            membership_type = input("Enter membership type (Regular, Student or Premium):  ")
            membership_start_date = input("Enter start date (YYYY-MM-DD):  ")
            membership_expiry_date = input("Enter expiry date (YYYY-MM-DD):  ")
            membership_status = input("Enter membership status (Active, Expired or Suspended):  ")
            outstanding_fees = float(input("Enter outstanding fees:  "))
            num_books_borrowed = int(input("Enter the number of books borrowed:  "))
            identification_document = input("Enter the ID number:  ")
            
            add_member(connection, first_name, last_name, date_of_birth, address, phone_number, email, membership_type, 
                       membership_start_date, membership_expiry_date, membership_status, outstanding_fees, 
                       num_books_borrowed, identification_document)
            
        elif choice == '3':
            print("Exiting program")
            break
        
        else:
            print()
            print("Invalid Choice")
        
        if connection:
            connection.close()
        
if __name__ == '__main__':
    main()