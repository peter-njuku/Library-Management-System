import pymysql
from pymysql import MySQLError
from datetime import datetime

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
        
        
def calculate_fine(return_date,due_date):
    if return_date and return_date > due_date:
        overdue_days = (return_date - due_date).days
        fine = overdue_days * 20
        return fine
    return 0
        
def add_transaction(connection, member_id, book_id, transaction_type, issue_date, due_date, return_date, transaction_status, notes):
    try:
        fine_amount = calculate_fine(return_date, due_date)
        with connection.cursor() as cursor:
            insert_query = """INSERT INTO transactions (member_id, book_id, transaction_type, issue_date, due_date, return_date, fine_amount, transaction_status, notes) 
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            transaction_data = (member_id, book_id,transaction_type, issue_date,due_date, return_date,fine_amount, transaction_status, notes)
            cursor.execute(insert_query, transaction_data)
            
        connection.commit()
        print("Transaction recorded successfully")
        return fine_amount
        
    except MySQLError as e:
        print("Error encounter when recording the transaction",e)


def main():
    connection = create_connection()
    
    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Add a book.")
        print("2. Add a new member.")
        print("3. Record a transaction.")
        print("4. Exit")
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
         
        elif choice == "3":
            member_id = int(input("Enter member ID:  "))
            book_id = input("Enter book ID:  ")
            transaction_type = input("Enter transaction type (Issue/Return):  ").capitalize()
            if transaction_type == "Issue":
                issue_date = input("Enter issue date (YYYY-MM-DD):  ")
                due_date = input("To be returned by date(YYYY-MM-DD):  ")
                return_date = None
                transaction_status = "Active"
                notes = input("Enter description: ")
                add_transaction(connection, member_id, book_id, transaction_type, issue_date, due_date, return_date, transaction_status, notes)
            
            elif transaction_type == "Return":
                return_date_input = input("Enter return date (YYYY-MM-DD): ")
                return_date = datetime.strptime(return_date_input, "%Y-%m-%d").date()  # Convert to date object
                issue_date_input = input("Enter issue date (YYYY-MM-DD): ")
                issue_date = datetime.strptime(issue_date_input, "%Y-%m-%d").date()
                due_date_input = input("Enter due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d").date()
                transaction_status = input("Enter transaction status (Active/Completed/Overdue): ")
                notes = input("Enter any additional notes: ")
                
                fine_amount = add_transaction(connection, member_id, book_id, transaction_type, issue_date, due_date, return_date, transaction_status, notes)
                
                if fine_amount is not None:
                    print(f"The fine amount is: Ksh{fine_amount:.2f}")
           
        elif choice == '4':
            print("Exiting program")
            break
        
        else:
            print()
            print("Invalid Choice")
        
        if connection:
            connection.close()
        
if __name__ == '__main__':
    main()