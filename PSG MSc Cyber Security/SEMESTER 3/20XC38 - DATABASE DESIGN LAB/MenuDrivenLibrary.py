import cx_Oracle
import sys

# FUNCTION TO PRINT ADMIN MENU
def print_admin_menu():
    print("\n\n--------------------  ADMIN  --------------------")
    print("1. ADD A BOOK")
    print("2. REMOVE A BOOK USING BOOK ID")
    print("3. VIEW ALL CUSTOMER DETAILS")
    print("4. EXIT\n")


# FUNCTION TO PRINT THE USER MENU
def print_user_menu():
    print("\n\n--------------------  USER  --------------------")
    print("1. VIEW BOOK DETAILS USING BOOK ID")
    print("2. VIEW MY RENT INFORMATION")
    print("3. RENT A BOOK")
    print("4. PAY FINES")
    print("5. UPDATE MY DETAILS")
    print("6. VIEW ALL BOOK DETAILS")
    print("7. VIEW MY DETAILS")
    print("8. RETURN BOOK")
    print("9. EXIT\n")
    

# FUNCTION TO GET DBMS_OUTPUT
def get_output(cursor):
    status = cursor.var(cx_Oracle.NUMBER)
    line = cursor.var(cx_Oracle.STRING)
    lines = []
    while True:
        cursor.callproc('DBMS_OUTPUT.GET_LINE', (line, status))
        if status.getvalue() == 0:
            lines.append(line.getvalue())
        else:
            break
    return lines


myconnection = cx_Oracle.connect(user='vary',password='SVar1145',dsn='')
cursor = myconnection.cursor()
cursor.callproc('DBMS_OUTPUT.ENABLE')

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LIBRARY MANAGEMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("1. ADMIN\n2. USER\n3. EXIT")
firstChoice = int(input("\nENTER OPTION NUMBER: "))
if firstChoice == 1:
    admin_user = input("ENTER ADMIN USERNAME: ")
    admin_pass = input("ENTER ADMIN PASSWORD: ")
    if admin_user == "admin" and admin_pass == "admin123":
        while True:
            print_admin_menu()
            adminchoice = int(input("ENTER OPTION NUMBER: "))
            if adminchoice == 1:
                isbn = input("ENTER ISBN OF BOOK: ")
                bookid = input("ENTER BOOKID: ")
                state = input("ENTER STATE OF THE BOOK: ")
                debycost = int(input("ENTER DEBY COST: "))
                lostcost = int(input("ENTER LOST COST: "))
                cursor.callproc('ADMIN_PACKAGE.addBook_library', [isbn, bookid, state, debycost, lostcost])
                resultInsert = get_output(cursor)
                myconnection.commit()
                print("\n\n")
                for i in resultInsert:
                    print(i)
            elif adminchoice == 2:
                bookid = input("ENTER BOOK ID: ")
                cursor.callproc('ADMIN_PACKAGE.removeItem_library', [bookid])
                resultRemove = get_output(cursor)
                myconnection.commit()
                print("\n\n")
                for i in resultRemove:
                    print(i)
            elif adminchoice == 3:
                cursor.callproc('ADMIN_PACKAGE.ViewAllCustomerDetails')
                customerdetails = get_output(cursor)
                print("\n\n")
                for i in customerdetails:
                    print(i)
            else:
                print("\n\nTHANK YOU. PLEASE VISIT NEXT TIME.\n\n")
                sys.exit()
    else:
        print("\nUNAUTHORISED ACCESS.\n")
        sys.exit()
elif firstChoice == 2:
    print("\n1. LOGIN\n2. SIGNUP\n")
    login_or_signup = int(input("\nENTER OPTION: "))
    if login_or_signup == 1:
        username = input("ENTER USERNAME: ")
        password = input("ENTER PASSWORD: ")
        cursor.callproc('USER_PACKAGE.loginCustomer_library', (username, password))
        result_log_in = get_output(cursor)
        print("\n\n")
        for i in result_log_in:
            print(i)
        if f"User {username} loging succesfull" in result_log_in:
            cursor.execute(f"SELECT CUSTOMERID, CARDNUMBER FROM CUSTOMER WHERE USERNAME = '{username}'")
            details = cursor.fetchone()
            customerid = details[0]
            cardnumber = details[1]
            while True:
                print_user_menu()
                user_choice = int(input("ENTER OPTION NUMBER: "))
                if user_choice == 1:
                    bookid = input('ENTER BOOK ID: ')
                    cursor.callproc('USER_PACKAGE.viewItem_library', [bookid])
                    bookdetail = get_output(cursor)
                    print("\n")
                    for i in bookdetail:
                        print(i)
                elif user_choice == 2:
                    cursor.callproc('USER_PACKAGE.customerAccount_library', [cardnumber])
                    rent_info = get_output(cursor)
                    print("\n")
                    for i in rent_info:
                        print(i)
                elif user_choice == 3:
                    bookid = input('ENTER BOOK ID: ')
                    date = input('ENTER RETURN DATE(dd-mmm-yy): ')
                    cursor.callproc('USER_PACKAGE.rentItem_library', [cardnumber, bookid, date])
                    rent_result = get_output(cursor)
                    myconnection.commit()
                    print("\n")
                    for i in rent_result:
                        print(i)
                elif user_choice == 4:
                    money = int(input("ENTER THE MONEY YOU ARE GOING TO PAY AS FINE: "))
                    cursor.callproc('USER_PACKAGE.payFines_library', [cardnumber, money])
                    payFineResult = get_output(cursor)
                    myconnection.commit()
                    for i in payFineResult:
                        print(i)
                elif user_choice == 5:
                    address = input("ENTER ADDRESS: ")
                    phone = int(input("ENTER PHONE NUMBER: "))
                    new_pass = input("ENTER NEW PASSWORD: ")
                    cursor.callproc('USER_PACKAGE.updateInfoCusto_library', [customerid, phone, address, new_pass])
                    updated_details = get_output(cursor)
                    myconnection.commit()
                    print("\n")
                    for i in updated_details:
                        print(i)
                elif user_choice == 6:
                    cursor.callproc('USER_PACKAGE.allBooks_library')
                    bookdetails = get_output(cursor)
                    print("\n")
                    for i in bookdetails:
                        print(i)
                elif user_choice == 7:
                    cursor.callproc('USER_PACKAGE.viewCustomer_library', [customerid])
                    customerdetail = get_output(cursor)
                    print("\n")
                    for i in customerdetail:
                        print(i)
                elif user_choice == 8:
                    bookid = input("ENTER BOOK ID OF THE BOOK TO BE RETURNED: ")
                    cursor.callproc('USER_PACKAGE.handleReturns_library', [bookid])
                    returnBookResult = get_output(cursor)
                    myconnection.commit()
                    print("\n")
                    for i in returnBookResult:
                        print(i)
                else:
                    print("\n\nTHANK YOU. PLEASE VISIT NEXT TIME.\n\n")
                    sys.exit()
                
                
    elif login_or_signup == 2:
        name = input("ENTER NAME: ")
        address = input("ENTER ADDRESS: ")
        phone = int(input("ENTER PHONE NUMBER: "))
        username = input("ENTER USERNAME: ")
        password = input("ENTER PASSWORD: ")
        cursor.callproc('USER_PACKAGE.addCustomer_library', [name, address, phone, username, password])
        signupResult = get_output(cursor)
        myconnection.commit()
        print("\n\n")
        for i in signupResult:
            print(i)
        
else:
    print("\n\nTHANK YOU. PLEASE VISIT NEXT TIME.\n\n")

myconnection.close()
