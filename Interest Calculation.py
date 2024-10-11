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
