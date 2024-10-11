# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:07:02 2024

@author: Asus
"""


import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="mysql123",  # Replace with your MySQL password
        database="bank_management"
    )

import random

def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

def create_account(name, address, phone_number, account_type, initial_deposit):
    db = connect_to_db()
    cursor = db.cursor()
    
    account_number = generate_account_number()
    
    sql = """INSERT INTO Customers (name, address, phone_number, account_number, balance, account_type) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
    
    values = (name, address, phone_number, account_number, initial_deposit, account_type)
    cursor.execute(sql, values)
    db.commit()
    
    print(f"Account created successfully! Account Number: {account_number}")
    
    cursor.close()
    db.close()