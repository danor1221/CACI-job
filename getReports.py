# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:06:49 2022

@author: danor
"""

import sqlite3, time



def getFradulentTransactions():
    
    print("Number of fradulent transactions in transaction001 is: ")
    
    query = """
                select count(transaction001.credit_card_number)
                from transaction001 
                inner join fraud 
                on transaction001.credit_card_number = fraud.credit_card_number;
            """
    callQueryNum(query)
    time.sleep(1)
    
    
    
    print("Number of fradulent transactions in transaction002 is: ")
    
    query = """
                select count(transaction002.credit_card_number)
                from transaction002 
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number;
            """
    callQueryNum(query)
    time.sleep(1)
    
    
    
    print("Distribution of fradulent transactions by state:")
    
    query = """
                select transaction002.state, count(transaction002.credit_card_number)
                from transaction002
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number
                group by transaction002.state;
            """
    callQueryAll(query)
    time.sleep(1)
    
    
    
    print ("Distribution of fradulent transactions by card vendor:")
    
    query = """
                select transaction002.vendor, count(transaction002.credit_card_number)
                from transaction002
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number
                group by transaction002.vendor
            """
    callQueryAll(query)
    
    





def callQueryNum(query):
    conn = sqlite3.connect('SQLDatabase10.db')
    cur = conn.cursor()
    
    try:
        cur.execute(query)
        print(cur.fetchone()[0])
    except:
        print("Bad query, try again")
        raise

    conn.close()

def callQueryAll(query):
    conn = sqlite3.connect('SQLDatabase10.db')
    cur = conn.cursor()
    
    try:
        cur.execute(query)
        print(cur.fetchall())
    except:
        print("Bad query, try again")
        raise

    conn.close()







if __name__ == "__main__":
    getFradulentTransactions()
