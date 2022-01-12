# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:01:42 2022

@author: danor
"""

import sqlite3

from fraudData import insert_fraud_values
from transaction001Data import insert_transaction001_values
from transaction002Data import insert_transaction002_values


def generate_tables():
    
    conn = sqlite3.connect('SQLDatabase6.db')
    
    cur = conn.cursor()
    
    
    cur.execute("""CREATE TABLE fraud (
                credit_card_number BIGINT,
                ipv4 VARCHAR(15),
                state VARCHAR(2)
                );
                """)
    
    cur.execute(insert_fraud_values)
    
    cur.execute("""CREATE TABLE transaction001 (
                credit_card_number BIGINT,
                ipv4 VARCHAR(15),
                state VARCHAR(2)
                );
                """)
    
    cur.execute(insert_transaction001_values)
    
    cur.execute("""CREATE TABLE transaction002 (
                credit_card_number BIGINT,
                ipv4 VARCHAR(15),
                state VARCHAR(2)
                );
                """)
    
    cur.execute(insert_transaction002_values)
    
    
    conn.commit()
    conn.close()




if __name__ == "__main__":
    generate_tables()

