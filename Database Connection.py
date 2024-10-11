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
