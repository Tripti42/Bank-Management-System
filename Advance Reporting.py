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

