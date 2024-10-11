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
