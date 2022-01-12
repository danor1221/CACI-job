# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:06:49 2022

@author: danor
"""

import sqlite3, time

from sanitiser import sanitise

def getFradulentTransactions():
    
    conn = sqlite3.connect('SQLDatabase6.db')
    cur = conn.cursor()
    
    
    
    print("Number of fradulent transactions in transaction001 is: ")
    
    cur.execute("""select count(transaction001.credit_card_number)
                from transaction001 
                inner join fraud 
                on transaction001.credit_card_number = fraud.credit_card_number;
                """)
    print(cur.fetchone()[0])
    time.sleep(1)
    
    
    
    print("Number of fradulent transactions in transaction002 is: ")
    
    cur.execute("""select count(transaction002.credit_card_number)
                from transaction002 
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number;
                """)
    print(cur.fetchone()[0])
    time.sleep(1)
    
    
    
    print("Distribution of fradulent transactions by state:")
    
    cur.execute("""select transaction002.state, count(transaction002.credit_card_number)
                from transaction002
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number
                group by transaction002.state;
                """)
    print(cur.fetchall())
    time.sleep(1)
    
    
    
    print ("Distribution of fradulent transactions by card vendor:")
    
    cur.execute("""select transaction002.vendor, count(transaction002.credit_card_number)
                from transaction002
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number
                group by transaction002.vendor
                """)
    print(cur.fetchall())
    
    
    
    conn.close()



if __name__ == "__main__":
    getFradulentTransactions()
