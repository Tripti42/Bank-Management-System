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
