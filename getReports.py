# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:06:49 2022

@author: danor
"""

import sqlite3
import time
import json
import collections



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
    
    
    
    print ("Obtain Json of masked fradulent transactions")
    
    query = """
                select transaction002.credit_card_number, transaction002.ipv4, transaction002.state
                from transaction002
                inner join fraud
                on transaction002.credit_card_number = fraud.credit_card_number
            """
    conn = sqlite3.connect('SQLDatabase.db')
    cur = conn.cursor()
    
    cur.execute(query)
    rows = cur.fetchall()
    
    
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        
        asStr = str(row[0])
        size = len(asStr)
        replacement = "*********"
        asStr = asStr.replace(asStr[size - 9:], replacement)

        d['credit_card_number'] = asStr
        d['ipv4'] = row[1]
        d['state'] = row[2]
        objects_list.append(d)
    
    json_output = json.dumps(objects_list)
    
    with open("returnJSON.js", "w") as f:
        f.write(json_output)
    
    conn.close()

    




def callQueryNum(query):
    conn = sqlite3.connect('SQLDatabase.db')
    cur = conn.cursor()
    
    try:
        cur.execute(query)
        print(cur.fetchone()[0])
    except:
        print("Bad query, try again")
        raise

    conn.close()

def callQueryAll(query):
    conn = sqlite3.connect('SQLDatabase.db')
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
