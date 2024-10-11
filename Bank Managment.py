# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:07:02 2024

@author: Asus
"""
import mysql.connector
import random
import bcrypt
import tkinter as tk
from tkinter import messagebox


import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="mysql123",  # Replace with your MySQL password
        database="bank_management"
    )



# Account Creation

def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

def create_account_with_password(name, address, phone_number, account_type, initial_deposit, password):
    db = connect_to_db()
    cursor = db.cursor()
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    sql = """INSERT INTO Customers (name, address, phone_number, account_number, balance, account_type, password) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    
    account_number = generate_account_number()
    values = (name, address, phone_number, account_number, initial_deposit, account_type, hashed_password)
    cursor.execute(sql, values)
    db.commit()
    
    print(f"Account created successfully! Account Number: {account_number}")
    cursor.close()
    db.close()


# Password Verification

def verify_password(account_number, password):
    db = connect_to_db()
    cursor = db.cursor()
    
    sql = "SELECT password FROM Customers WHERE account_number = %s"
    cursor.execute(sql, (account_number,))
    stored_password = cursor.fetchone()[0]
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False
    
    cursor.close()
    db.close()



#  Deposit/Withdraw with Transaction Logging

def get_customer_id(account_number):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT customer_id FROM Customers WHERE account_number = %s", (account_number,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0] if result else None

def update_balance(account_number, amount, transaction_type):
    db = connect_to_db()
    cursor = db.cursor()

    # Update the balance in the Customers table
    if transaction_type == 'deposit':
        sql = "UPDATE Customers SET balance = balance + %s WHERE account_number = %s"
    elif transaction_type == 'withdraw':
        sql = "UPDATE Customers SET balance = balance - %s WHERE account_number = %s"
    
    cursor.execute(sql, (amount, account_number))

    # Log the transaction in the Transactions table
    customer_id = get_customer_id(account_number)
    if customer_id:
        sql = """INSERT INTO Transactions (customer_id, date, transaction_type, amount)
                 VALUES (%s, CURDATE(), %s, %s)"""
        cursor.execute(sql, (customer_id, transaction_type, amount))
        db.commit()
        print(f"{transaction_type.capitalize()} successful!")
    else:
        print("Account not found!")
    
    cursor.close()
    db.close()
    
    
# Interest Calculation


def apply_interest(account_type='savings', interest_rate=0.03):
    db = connect_to_db()
    cursor = db.cursor()

    # Update balance for all savings accounts by adding interest
    sql = """UPDATE Customers 
             SET balance = balance + (balance * %s) 
             WHERE account_type = %s"""
    
    cursor.execute(sql, (interest_rate, account_type))
    db.commit()
    
    print(f"Interest applied to all {account_type} accounts!")
    cursor.close()
    db.close()


# Advanced Reporting

def generate_report():
    db = connect_to_db()
    cursor = db.cursor()

    # Total number of accounts
    cursor.execute("SELECT COUNT(*) FROM Customers")
    total_accounts = cursor.fetchone()[0]
    
    # Total deposits and withdrawals
    cursor.execute("SELECT SUM(amount) FROM Transactions WHERE transaction_type = 'deposit'")
    total_deposits = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT SUM(amount) FROM Transactions WHERE transaction_type = 'withdraw'")
    total_withdrawals = cursor.fetchone()[0] or 0
    
    # Total balance in all accounts
    cursor.execute("SELECT SUM(balance) FROM Customers")
    total_balance = cursor.fetchone()[0] or 0
    
    print(f"Total Accounts: {total_accounts}")
    print(f"Total Deposits: {total_deposits}")
    print(f"Total Withdrawals: {total_withdrawals}")
    print(f"Total Balance in All Accounts: {total_balance}")

    cursor.close()
    db.close()


# Account Deletion

def delete_account(account_number):
    db = connect_to_db()
    cursor = db.cursor()

    # First, delete all transactions related to this account
    customer_id = get_customer_id(account_number)
    if customer_id:
        cursor.execute("DELETE FROM Transactions WHERE customer_id = %s", (customer_id,))
        
        # Then, delete the customer account
        cursor.execute("DELETE FROM Customers WHERE account_number = %s", (account_number,))
        db.commit()
        
        print("Account and all related transactions deleted successfully!")
    else:
        print("Account not found!")
    
    cursor.close()
    db.close()
    
# Creating GUI    
    
def create_account_gui():
    def submit():
        name = name_entry.get()
        address = address_entry.get()
        phone = phone_entry.get()
        account_type = account_type_entry.get()
        initial_deposit = float(initial_deposit_entry.get())
        password = password_entry.get()

        create_account_with_password(name, address, phone, account_type, initial_deposit, password)
        messagebox.showinfo("Success", f"Account created for {name}!")
        window.destroy()
    
    window = tk.Tk()
    window.title("Create New Account")
    
    tk.Label(window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)
    
    tk.Label(window, text="Address:").grid(row=1, column=0)
    address_entry = tk.Entry(window)
    address_entry.grid(row=1, column=1)
    
    tk.Label(window, text="Phone Number:").grid(row=2, column=0)
    phone_entry = tk.Entry(window)
    phone_entry.grid(row=2, column=1)
    
    tk.Label(window, text="Account Type:").grid(row=3, column=0)
    account_type_entry = tk.Entry(window)
    account_type_entry.grid(row=3, column=1)
    
    tk.Label(window, text="Initial Deposit:").grid(row=4, column=0)
    initial_deposit_entry = tk.Entry(window)
    initial_deposit_entry.grid(row=4, column=1)

    tk.Label(window, text="Password:").grid(row=5, column=0)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=5, column=1)
    
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=6, column=1)

    window.mainloop()



# Main Program


def main_menu():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. View account details")
        print("5. View transaction history")
        print("6. Apply interest")
        print("7. Generate report")
        print("8. Delete an account")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account_gui()
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            update_balance(account_number, amount, 'deposit')
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            update_balance(account_number, amount, 'withdraw')
        elif choice == '4':
            account_number = input("Enter account number: ")
             # Fetch and display account details here
        elif choice == '5':
             print()
             # Fetch and display transaction history here
        elif choice == '6':
            apply_interest()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            account_number = input("Enter account number to delete: ")
            delete_account(account_number)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

