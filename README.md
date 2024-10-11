## **Bank Management System**

This project is a simple Bank Management System built using Python, MySQL, and a basic Tkinter graphical user interface (GUI). The system allows you to create accounts, deposit or withdraw money, track transactions, and more.



![image](https://github.com/user-attachments/assets/e3a5d539-9c0c-4121-97fc-c5bf793a8577)




## **Features**

Create Account: Open a new account with a secure password.

Password Security: Passwords are stored securely using hashing.

Deposit/Withdraw Money: Easily add or take out money from accounts.

Transaction History: Track all deposits and withdrawals.

Interest Calculation: Apply interest to savings accounts.

Delete Account: Remove accounts and their transaction history.

Reporting: Get reports on the total number of accounts, deposits, and balance.

GUI: Use a simple Tkinter window for creating accounts and other operations.




## **Technologies Used**

Python: The main programming language.

MySQL: The database to store account and transaction data.

Tkinter: To create a simple window for user interaction.




## **Prerequisites**

Python 3.x must be installed on your computer.

MySQL must be installed and running.

Install the necessary Python libraries by running:

pip install mysql-connector-python bcrypt tkinter



## **Database Setup**

Open MySQL and create the database:

**Creating the Database**

CREATE DATABASE bank_management;
USE bank_management;
Create the tables:


## **Creating the Tables**


CREATE TABLE Customers (

    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(15),
    account_number VARCHAR(20) UNIQUE,
    balance DECIMAL(10, 2),
    account_type VARCHAR(20),
    password VARCHAR(255)
);

CREATE TABLE Transactions (

    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    date DATE,
    transaction_type VARCHAR(50),
    amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);





**python code **

## **Connecting the Database **

def connect_to_db():

    return mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="mysql123",  # Your MySQL password
        database="bank_management"
    )






## **How the System Works**


Create Account: Enter customer details to create a new account.

Login: You can log in using your account number and password.

Deposit/Withdraw: Choose an account to deposit or withdraw money.

Transaction History: View all transactions made for an account.

Interest Calculation: Automatically apply interest to savings accounts.

Report: Get a summary of the total number of accounts, deposits, withdrawals, and balance.



