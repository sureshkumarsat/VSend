SET SERVEROUTPUT ON;


--LIBRARY PROJECT--

----CREATE TABLES--

CREATE TABLE Card(
  cardID NUMBER,
  status VARCHAR2(1) CHECK ((status = 'A') OR (status = 'B')),
  fines NUMBER,
  CONSTRAINT Card_PK PRIMARY KEY (cardID));


CREATE TABLE Customer(
  customerID NUMBER,
  name VARCHAR2(40),
  customerAddress VARCHAR2(50),
  phone NUMBER(9),
  password VARCHAR2(20),
  userName VARCHAR2(10),
  dateSignUp DATE,
  cardNumber NUMBER,
  CONSTRAINT Customer_PK PRIMARY KEY (customerID));

  
CREATE TABLE Rent(
  cardID NUMBER,
  itemID VARCHAR2(6),
  apporpriationDate DATE,
  returnDate DATE);

 
CREATE TABLE Book(
  ISBN VARCHAR2(4),
  bookID VARCHAR2(6),
  state VARCHAR2(10),
  avalability VARCHAR2(1) CHECK ((avalability = 'A') OR (avalability = 'O')),
  debyCost NUMBER(10,2),
  lostCost NUMBER(10,2),
  CONSTRAINT Book_PK PRIMARY KEY (bookID));


----DROP TABLES--

--DROP TABLE Card;
--DROP TABLE Customer;
--DROP TABLE Book;
--DROP TABLE Rent;


----FOREIGN KEYS--
ALTER TABLE Customer
ADD CONSTRAINT Customer_FK
FOREIGN KEY (cardNumber)
REFERENCES Card(cardID);


ALTER TABLE Rent
ADD CONSTRAINT Rent_FK_Card
FOREIGN KEY (cardID)
REFERENCES Card(cardID);

ALTER TABLE Rent
ADD CONSTRAINT Rent_FK_Book
FOREIGN KEY (itemID)
REFERENCES Book(bookID);


--INSERT SAMPLE DATA--

INSERT INTO Card VALUES (101,'A',0);
INSERT INTO Card VALUES (102,'A',0);
INSERT INTO Card VALUES (103,'A',0);
INSERT INTO Card VALUES (104,'A',0);
INSERT INTO Card VALUES (105,'A',0);
INSERT INTO Card VALUES (106,'A',0);
INSERT INTO Card VALUES (107,'B',50);
INSERT INTO Card VALUES (108,'B',10);
INSERT INTO Card VALUES (109,'B',25.5);
INSERT INTO Card VALUES (110,'B',15.25);
INSERT INTO Card VALUES (151,'A',0);
INSERT INTO Card VALUES (152,'A',0);
INSERT INTO Card VALUES (153,'A',0);
INSERT INTO Card VALUES (154,'A',0);
INSERT INTO Card VALUES (155,'A',0);


INSERT INTO Customer VALUES (1, 'ALFRED', 'BACON STREET', 623623623, 'alfred123', 'al1', '12-05-2018', 101);
INSERT INTO Customer VALUES (2, 'JAMES', 'DOWNTOWN ABBEY', 659659659, 'james123', 'ja2', '10-05-2018', 102);
INSERT INTO Customer VALUES (3, 'GEORGE', 'DETROIT CITY', 654654654, 'george123', 'ge3', '21-06-2017', 103);
INSERT INTO Customer VALUES (4, 'TOM', 'WASHINGTON DC.', 658658658, 'tom123', 'tom4', '05-12-2016', 104);
INSERT INTO Customer VALUES (5, 'PETER', 'CASTERLY ROCK', 652652652, 'peter123', 'pe5', '09-08-2016', 105);
INSERT INTO Customer VALUES (6, 'JENNY', 'TERRAKOTA', 651651651, 'jenny123', 'je6', '30-04-2017', 106);
INSERT INTO Customer VALUES (7, 'ROSE', 'SWEET HOME ALABAMA', 657657657, 'rose123', 'ro7', '28-02-2018', 107);
INSERT INTO Customer VALUES (8, 'MONICA', 'FAKE STREET 123', 639639639, 'monica123', 'mo8', '15-01-2016', 108);
INSERT INTO Customer VALUES (9, 'PHOEBE', 'CENTRAL PERK', 678678678, 'phoebe123', 'pho9', '25-03-2016', 109);
INSERT INTO Customer VALUES (10, 'RACHEL', 'WHEREVER', 687687687, 'rachel123', 'ra10', '01-09-2017', 110);


INSERT INTO Book VALUES ('A123', 'B1A123', 'GOOD', 'A', 5, 20);
INSERT INTO Book VALUES ('A123', 'B2A123', 'NEW', 'O', 6, 30);
INSERT INTO Book VALUES ('B234', 'B1B234', 'NEW', 'A', 2, 15);
INSERT INTO Book VALUES ('C321', 'B1C321', 'BAD', 'A', 1, 10);
INSERT INTO Book VALUES ('H123', 'B1H123', 'GOOD', 'A', 3, 15);
INSERT INTO Book VALUES ('Z123', 'B1Z123', 'GOOD', 'O', 4, 20);
INSERT INTO Book VALUES ('L321', 'B1L321', 'NEW', 'O', 4, 20);
INSERT INTO Book VALUES ('P321', 'B1P321', 'USED', 'A', 2, 12);


INSERT INTO Rent VALUES (101, 'B2A123', '10-05-2018', '20-05-2018');
INSERT INTO Rent VALUES (102, 'B1Z123', '10-05-2018', '25-05-2018');
INSERT INTO Rent VALUES (154, 'B1L321', '04-05-2018', '26-05-2018');


--SELECT--
SELECT * FROM Card;
SELECT * FROM Customer;
SELECT * FROM Book;
SELECT * FROM Rent;


--PUTTING PROCEDURES AND TRIGGERS INTO 2 PACKAGES--


---------- ADMIN PACKAGE ----------


CREATE OR REPLACE PACKAGE ADMIN_PACKAGE AS
    -- ADD BOOK 
    PROCEDURE addBook_library(auxISBN IN BOOK.ISBN%TYPE, auxBookID IN BOOK.BOOKID%TYPE, auxState IN BOOK.STATE%TYPE, auxDebyCost IN BOOK.DEBYCOST%TYPE, auxLostCost IN BOOK.LOSTCOST%TYPE);

    -- REMOVE BOOK USING BOOK ID
    PROCEDURE removeItem_library(auxItemID IN BOOK.BOOKID%TYPE);
    
    -- LISTS ALL CUSTOMERS
    PROCEDURE ViewAllCustomerDetails;
END ADMIN_PACKAGE;
/


CREATE OR REPLACE PACKAGE BODY ADMIN_PACKAGE AS
    
    -- ADD BOOK
    PROCEDURE addBook_library(auxISBN IN BOOK.ISBN%TYPE, auxBookID IN BOOK.BOOKID%TYPE, auxState IN BOOK.STATE%TYPE, auxDebyCost IN BOOK.DEBYCOST%TYPE,
    auxLostCost IN BOOK.LOSTCOST%TYPE)
    IS
    BEGIN
        INSERT INTO book
        VALUES(auxISBN,auxBookID,auxState,'A',auxDebyCost,auxLostCost);
        DBMS_OUTPUT.PUT_LINE('Book inserted correctly');
        EXCEPTION
            WHEN DUP_VAL_ON_INDEX THEN
                DBMS_OUTPUT.PUT_LINE('BOOK ID ALREADY EXISTS.');
    END ADDBOOK_LIBRARY;
    
    -- REMOVE BOOK USING BOOK ID
    PROCEDURE removeItem_library(auxItemID IN BOOK.BOOKID%TYPE)
    IS
        auxBook NUMBER;
        avail BOOK.AVALABILITY%TYPE;
    BEGIN
        SELECT COUNT(*) INTO auxBook
        FROM book
        WHERE bookid LIKE auxItemID;
    
        SELECT AVALABILITY INTO AVAIL
        FROM BOOK
        WHERE BOOKID LIKE AUXITEMID;
    
        IF auxBook > 0 THEN
            IF avail = 'A' THEN
                DELETE FROM book
                WHERE bookid LIKE auxItemID;
                DBMS_OUTPUT.PUT_LINE('Book removed correctly');
            ELSE
                DBMS_OUTPUT.PUT_LINE('BOOK HAS BEEN BORROWED. CANNOT REMOVE NOW.');
            END IF;
        ELSE
            DBMS_OUTPUT.PUT_LINE('Book does not exist in records');
        END IF;
    END removeitem_library;
    
    -- LIST ALL CUSTOMER DETAILS
    PROCEDURE ViewAllCustomerDetails
    IS
        CURSOR cCust
        IS
        SELECT *
        FROM CUSTOMER;
    
        xCust cCust%ROWTYPE;
    BEGIN
        OPEN cCust;
    
        DBMS_OUTPUT.PUT_LINE('CUSTOMERID     NAME    CUSTOMERADRESS    PHONE    USERNAME    CARDNUMBER');
        DBMS_OUTPUT.PUT_LINE('------------------------------------------------------------------------');
    
        LOOP
            FETCH cCust
            INTO xCust;
            EXIT WHEN cCust%NOTFOUND;
    
            DBMS_OUTPUT.PUT_LINE(xCust.CUSTOMERID || '     ' || xCust.NAME || '     ' || xCust.CUSTOMERADDRESS || '          ' || xCust.PHONE || '               ' || xCust.USERNAME || '          ' ||
            xCust.CARDNUMBER || '     ');
        END LOOP;
    END ViewAllCustomerDetails;
        
END ADMIN_PACKAGE;
/


---------- USER PACKAGE ----------


CREATE OR REPLACE PACKAGE USER_PACKAGE AS
    -- USER LOGIN
    PROCEDURE loginCustomer_library(user IN CUSTOMER.USERNAME%TYPE, pass IN CUSTOMER.PASSWORD%TYPE);
    
    -- VIEW BOOK DETAILS USING BOOK ID
    PROCEDURE viewItem_library(auxItemID IN BOOK.BOOKID%TYPE);
    
    -- VIEW RENT DETAILS OF USER
    PROCEDURE customerAccount_library(custoCard IN customer.CARDNUMBER%TYPE);
    
    -- RENT BOOK
    PROCEDURE rentItem_library(auxCard IN CARD.CARDID%TYPE, auxItemID IN BOOK.BOOKID%TYPE, auxDate IN RENT.RETURNDATE%TYPE);

    -- PAY FINES
    PROCEDURE payFines_library(auxCard IN card.cardid%TYPE, money IN NUMBER);
    
    -- UPDATING CUSTOMER INFORMATION
    PROCEDURE updateInfoCusto_library(auxCustomer IN customer.customerid%TYPE, pNumber IN CUSTOMER.PHONE%TYPE, address IN CUSTOMER.CUSTOMERADDRESS%TYPE, newPass CUSTOMER.PASSWORD%TYPE);

    -- ADD A NEW CUSTOMER
    PROCEDURE addCustomer_library(auxName IN CUSTOMER.NAME%TYPE, auxCustomerAddress IN CUSTOMER.CUSTOMERADDRESS%TYPE, auxPhone IN CUSTOMER.PHONE%TYPE, auxUserName IN CUSTOMER.USERNAME%TYPE, auxPass IN CUSTOMER.PASSWORD%TYPE);

    -- VIEW ALL BOOKS
    PROCEDURE allBooks_library;

    -- VIEW CUSTOMER DETAILS USING CUSTOMER ID
    PROCEDURE viewCustomer_library(auxCustomerID IN NUMBER);

    -- HANDLE RETURNS
    PROCEDURE handleReturns_library(auxItemID IN BOOK.BOOKID%TYPE);

END USER_PACKAGE;
/


CREATE OR REPLACE PACKAGE BODY USER_PACKAGE AS
    -- USER LOGIN
    PROCEDURE loginCustomer_library(user IN CUSTOMER.USERNAME%TYPE, pass IN CUSTOMER.PASSWORD%TYPE)
    IS
        passAux customer.password%TYPE;
        incorrect_password EXCEPTION;
    BEGIN
       
        SELECT password INTO passAux
        FROM Customer
        WHERE username = user;
        
        IF passAux = pass THEN
            DBMS_OUTPUT.PUT_LINE('User ' || user || ' loging succesfull');
        ELSE
            RAISE incorrect_password;
        END IF;
        
        EXCEPTION
            WHEN no_data_found OR incorrect_password THEN 
                DBMS_OUTPUT.PUT_LINE('Incorrect username or password');
    END loginCustomer_library;
    
    -- VIEW BOOK DETAILS USING BOOK ID
    PROCEDURE viewItem_library(auxItemID IN BOOK.BOOKID%TYPE)
    IS
        auxISBN BOOK.ISBN%TYPE;
        auxState BOOK.STATE%TYPE;
        auxDebyCost BOOK.DEBYCOST%TYPE;
        auxLostCost BOOK.LOSTCOST%TYPE;
        auxAbala VARCHAR2(1);
        auxBook NUMBER;
    BEGIN
      
        SELECT COUNT(*) INTO auxBook
        FROM book
        WHERE bookid LIKE auxItemID;
        
        IF auxBook > 0 THEN
            SELECT isbn, state, avalability, debycost, lostcost
            INTO auxISBN, auxState, auxAbala, auxDebyCost, auxLostCost
            FROM book
            WHERE bookid LIKE auxItemID;
            
            DBMS_OUTPUT.PUT_LINE('BOOK ' || auxItemID || ' INFO');
            DBMS_OUTPUT.PUT_LINE('------------------------------------------');
            DBMS_OUTPUT.PUT_LINE('ISBN: ' || auxISBN);
            DBMS_OUTPUT.PUT_LINE('STATE: ' || auxState);
            DBMS_OUTPUT.PUT_LINE('AVALABILITY: ' || auxAbala);
            DBMS_OUTPUT.PUT_LINE('DEBY COST: ' || auxDebyCost);
            DBMS_OUTPUT.PUT_LINE('LOST COST: ' || auxLostCost);
            DBMS_OUTPUT.PUT_LINE('------------------------------------------');
        
        ELSE
            DBMS_OUTPUT.PUT_LINE('BOOK NOT FOUND');
        
        END IF;
    END viewItem_library;

    --  CUSTOMER RENT INFORMATION
    PROCEDURE customerAccount_library(custoCard IN customer.CARDNUMBER%TYPE)
    IS
        CURSOR aCust
        IS
        SELECT * FROM RENT WHERE CARDID = custoCard;
        xCust aCust%ROWTYPE;
        auxFines NUMBER;
    BEGIN
        OPEN aCust;
        FETCH aCust INTO xCust;
        IF aCust%NOTFOUND THEN
            DBMS_OUTPUT.PUT_LINE('NO RENTS FOR THE USER REMAINING');
        ELSE
            DBMS_OUTPUT.PUT_LINE('THE BOOK IDS THE USER HAS RENTED IS: ');
            LOOP
                DBMS_OUTPUT.PUT_LINE('    ' || xCust.ITEMID);
                FETCH aCust
                INTO xCust;
                EXIT WHEN aCust%NOTFOUND;
                
                
            END LOOP;        
        END IF;
        
        SELECT fines INTO auxFines
        FROM card
        WHERE cardid LIKE custoCard;
        
        DBMS_OUTPUT.PUT_LINE('The user fines are ' || auxFines);
        
        EXCEPTION WHEN no_data_found THEN 
            DBMS_OUTPUT.PUT_LINE('NO DATA FOUND');
    END customerAccount_library;

    -- RENT BOOK
    PROCEDURE rentItem_library(auxCard IN CARD.CARDID%TYPE, auxItemID IN BOOK.BOOKID%TYPE, auxDate IN RENT.RETURNDATE%TYPE)
    IS
        statusAux CARD.STATUS%TYPE;
        avail BOOK.avalability%TYPE;
    BEGIN
      
        SELECT status INTO statusAux
        FROM card
        WHERE cardid LIKE auxCard;
        
        IF statusAux LIKE 'A' THEN
            SELECT avalability INTO avail
            FROM book
            WHERE bookid LIKE auxItemID;
            
            IF avail LIKE 'A' THEN
                UPDATE book
                SET avalability = 'O'
                WHERE bookid LIKE auxItemID;
                
                INSERT INTO rent
                VALUES (auxCard,auxItemID,sysdate,auxDate);
                DBMS_OUTPUT.PUT_LINE('Item ' || auxItemID || ' rented');
            ELSE
                DBMS_OUTPUT.PUT_LINE('The item is already rented');
            END IF;
        ELSE
            DBMS_OUTPUT.PUT_LINE('The user is blocked');
        END IF;    
        
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                DBMS_OUTPUT.PUT_LINE('WRONG DATA PROVIDED');
    END rentItem_library;

    -- PAY FINES
    PROCEDURE payFines_library(auxCard IN card.cardid%TYPE, money IN NUMBER)
    IS
        finesAmount NUMBER;
        total NUMBER;
    BEGIN
        SELECT fines INTO finesAmount
        FROM card
        WHERE cardid LIKE auxCard;
        
        IF finesAmount = 0 THEN
            DBMS_OUTPUT.PUT_LINE('YOU DO NOT HAVE TO PAY FINES AS YOUR FINE AMOUNT IS ALREADY 0.');
        ELSIF finesAmount < money THEN
            total := money - finesAmount;
            DBMS_OUTPUT.PUT_LINE('YOU HAVE PAYED ALL YOUR FINES AND YOU HAVE ' || total || ' MONEY BACK');
            
            UPDATE card
            SET status = 'A', fines = 0
            WHERE cardid = auxCard;
        
        ELSIF finesAmount = money THEN
            total := money - finesAmount;
            DBMS_OUTPUT.PUT_LINE('YOU HAVE PAYED ALL YOUR FINES');
        
            UPDATE card
            SET status = 'A', fines = 0
            WHERE cardid = auxCard;
      
        ELSE
            total := finesAmount - money;
            DBMS_OUTPUT.PUT_LINE('YOU WILL NEED TO PAY ' || total || ' MORE DOLLARS TO UNLOCK YOUR CARD');
            
            UPDATE card
            SET fines = total
            WHERE cardid = auxCard;
        END IF;
        
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                DBMS_OUTPUT.PUT_LINE('CARD ID DOES NOT EXIST.');
    END payFines_library;

    -- UPDATING CUSTOMER INFORMATION
    PROCEDURE updateInfoCusto_library(auxCustomer IN customer.customerid%TYPE, pNumber IN CUSTOMER.PHONE%TYPE, address IN CUSTOMER.CUSTOMERADDRESS%TYPE, newPass CUSTOMER.PASSWORD%TYPE)
    IS
        CURSOR Ccust
        IS
        SELECT * FROM CUSTOMER WHERE CUSTOMERID = auxcustomer;
        
        XCUST CCUST%ROWTYPE;
    BEGIN
        OPEN Ccust;
        FETCH CCUST INTO XCUST;
        IF CCUST%NOTFOUND THEN
            DBMS_OUTPUT.PUT_LINE('CUSTOMERID NOT FOUND IN RECORDS');
        ELSE
            UPDATE customer
            SET phone = pNumber, customeraddress = address, password = newPass
            WHERE customerid = auxCustomer;
            DBMS_OUTPUT.PUT_LINE('DETAILS UPDATED SUCCESSFULLY');
        END IF;
        
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                DBMS_OUTPUT.PUT_LINE('WRONG DETAILS PROVIDED');
            WHEN OTHERS THEN
                DBMS_OUTPUT.PUT_LINE('DATA TYPES HAVE EXCEEDED THEIR MAXIMUM VALUE LIMIT. ENTER DETAILS CORRECTLY.');
    END updateInfoCusto_library;

    -- ADD A NEW CUSTOMER
    PROCEDURE addCustomer_library(auxName IN CUSTOMER.NAME%TYPE, auxCustomerAddress IN CUSTOMER.CUSTOMERADDRESS%TYPE, auxPhone IN CUSTOMER.PHONE%TYPE,
    auxUserName IN CUSTOMER.USERNAME%TYPE, auxPass IN CUSTOMER.PASSWORD%TYPE)
    IS
        CURSOR USN
        IS
        SELECT * FROM CUSTOMER WHERE USERNAME =  auxusername;
        XUSN USN%ROWTYPE;
        CustID CUSTOMER.CUSTOMERID%TYPE;
        CardID CUSTOMER.CARDNUMBER%TYPE;
    BEGIN
        OPEN USN;
        SELECT MAX(CUSTOMERID) INTO CustID FROM CUSTOMER;
        CustID := CustID + 1;
        CardID := CustID + 100;
        FETCH USN INTO XUSN;
        IF USN%NOTFOUND THEN
            INSERT INTO customer VALUES (CustID,auxName,auxCustomerAddress,auxPhone,auxPass,auxUserName,sysdate,CardID);
            DBMS_OUTPUT.PUT_LINE('YOUR CUSTOMER ID IS: ' || CustID);
            DBMS_OUTPUT.PUT_LINE('YOUR CARD NUMBER IS: ' || CardID);
        ELSE
            DBMS_OUTPUT.PUT_LINE('THE USERNAME ALREADY EXISTS. TRY ANOTHER USERNAME.');
        END IF;
        
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                DBMS_OUTPUT.PUT_LINE('WRONG DETAILS PROVIDED');
            WHEN OTHERS THEN
                DBMS_OUTPUT.PUT_LINE('DATA TYPES HAVE EXCEEDED THEIR MAXIMUM VALUE LIMIT. ENTER DETAILS CORRECTLY.');
    END addCustomer_library;

    -- VIEW ALL BOOKS
    PROCEDURE allBooks_library
    IS
        CURSOR cBooks
        IS
        SELECT *
        FROM book;
      
        xBooks cBooks%ROWTYPE;
    BEGIN
        OPEN cBooks;
        
        DBMS_OUTPUT.PUT_LINE('ISBN     ID          STATE     AVALABILITY     DEBY COST     LOST COST    ');
        DBMS_OUTPUT.PUT_LINE('---------------------------------------------------------------------');
        
        LOOP
            FETCH cBooks
            INTO xBooks;
            EXIT WHEN cBooks%NOTFOUND;
            
            DBMS_OUTPUT.PUT_LINE(xBooks.isbn || '     ' || xBooks.bookid || '     ' || xBooks.state || '          ' || xBooks.avalability || '               ' || xBooks.debycost || '          ' ||
            xBooks.lostcost || '     ');
        END LOOP;
    END allBooks_library;

    -- VIEW CUSTOMER DETAILS USING CUSTOMER ID
    PROCEDURE viewCustomer_library(auxCustomerID IN NUMBER)
    IS
        custoName CUSTOMER.NAME%TYPE;
        custoAdd CUSTOMER.CUSTOMERADDRESS%TYPE;
        custoPhone CUSTOMER.PHONE%TYPE;
        userNaM CUSTOMER.USERNAME%TYPE;
        custoDate CUSTOMER.DATESIGNUP%TYPE;
        custoCard CUSTOMER.CARDNUMBER%TYPE;
    BEGIN
        SELECT name,customeraddress,phone,username,datesignup,cardnumber
        INTO custoName, custoAdd, custoPhone, userNaM, custoDate, custoCard
        FROM customer
        WHERE customerid LIKE auxCustomerID;
        
        DBMS_OUTPUT.PUT_LINE('CUSTOMER ' || auxCustomerID || ' INFO');
        DBMS_OUTPUT.PUT_LINE('------------------------------------------');
        DBMS_OUTPUT.PUT_LINE('NAME: ' || custoName);
        DBMS_OUTPUT.PUT_LINE('ADDRESS: ' || custoAdd);
        DBMS_OUTPUT.PUT_LINE('PHONE: ' || custoPhone);
        DBMS_OUTPUT.PUT_LINE('USER NAME: ' || userNaM);
        DBMS_OUTPUT.PUT_LINE('DATE OF SIGN UP: ' || custoDate);
        DBMS_OUTPUT.PUT_LINE('CARD NUMBER: ' || custoCard);
        DBMS_OUTPUT.PUT_LINE('------------------------------------------');
    
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            DBMS_OUTPUT.PUT_LINE('INVALID CUSTOMERID.');
    END viewCustomer_library;

    -- HANDLE RETURNS
    PROCEDURE handleReturns_library(auxItemID IN BOOK.BOOKID%TYPE)
    IS
        avail BOOK.AVALABILITY%TYPE;
        card RENT.CARDID%TYPE;
        bkID RENT.ITEMID%TYPE;
    BEGIN 
        SELECT AVALABILITY INTO avail
        FROM book
        WHERE bookid LIKE auxItemID;
                
        IF avail = 'O' THEN
            SELECT CARDID, ITEMID INTO card, bkID
            FROM RENT WHERE ITEMID = auxItemID;
            UPDATE book
            SET avalability = 'A'
            WHERE bookid = auxItemID;
            
            DELETE FROM rent
            WHERE CARDID = card AND itemid = auxItemID;
            DBMS_OUTPUT.PUT_LINE('The book ' || auxItemID || ' has been returned and is now avaible.');
            
        ELSIF avail = 'A' THEN
            DBMS_OUTPUT.PUT_LINE(auxItemID || ' HAS NOT BEEN RENTED.');
        END IF;
        
        EXCEPTION WHEN no_data_found THEN 
            DBMS_OUTPUT.PUT_LINE('ITEM ID DOESNT EXIST.');    
    END handleReturns_library;

END USER_PACKAGE;
/


-- TRIGGERS
-- ADD A NEW CUSTOMER TRIGGER
CREATE OR REPLACE TRIGGER addCardCusto_library
AFTER INSERT
ON customer
FOR EACH ROW
DECLARE
BEGIN
    INSERT INTO card
    VALUES (:new.cardnumber,'A',0);
    
    DBMS_OUTPUT.PUT_LINE('Card created');
END;
/

-- RETURNING BOOK TRIGGER
CREATE OR REPLACE TRIGGER modifyFines_library
AFTER DELETE
ON rent
FOR EACH ROW
DECLARE
    auxCardID CARD.CARDID%TYPE := :old.cardid;
    auxItemID BOOK.BOOKID%TYPE := :old.itemid;
    auxDeby BOOK.DEBYCOST%TYPE;
BEGIN
    IF sysdate > :old.returndate THEN
        SELECT debyCost INTO auxDeby
        FROM book
        WHERE bookid LIKE auxItemID;
    
        UPDATE card
        SET status = 'B', fines = (fines + auxDeby)
        WHERE cardid LIKE auxCardID;
        DBMS_OUTPUT.PUT_LINE(auxCardID || ' has to pay extra fine of ' || auxDeby);
    ELSE
        DBMS_OUTPUT.PUT_LINE('The item has been returned before deadline');
    END IF;
END;
/


SET SERVEROUTPUT ON;