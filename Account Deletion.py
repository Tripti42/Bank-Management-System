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

