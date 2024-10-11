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
