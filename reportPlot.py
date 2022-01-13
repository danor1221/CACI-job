# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:49:35 2022

@author: danor
"""

import sqlite3
import numpy as np
import matplotlib.pyplot as plt


def plotReports():
    conn = sqlite3.connect('SQLDatabase.db')
    cur = conn.cursor()
    
    queryState = """
                select transaction002.state, count(transaction002.credit_card_number)
                from transaction002
                inner join fraud 
                on transaction002.credit_card_number = fraud.credit_card_number
                group by transaction002.state;
            """
    
    cur.execute(queryState)
    dataState = cur.fetchall()
    
    
    #plt.plot(x_pos, trendline, color='red', linestyle='--')    
    plt.bar(range(len(dataState)), [val[1] for val in dataState], align='center')
    plt.xticks(range(len(dataState)), [val[0] for val in dataState]) 
    plt.xticks(rotation=80, fontsize=6)
    plt.ylabel('no. Fradulent Transactions')
    plt.plot()
    plt.show()
    
    
    
    
    queryVendor = """
                    select transaction002.vendor, count(transaction002.credit_card_number)
                    from transaction002
                    inner join fraud 
                    on transaction002.credit_card_number = fraud.credit_card_number
                    group by transaction002.vendor
                  """
    
    cur.execute(queryVendor)
    dataVendor = cur.fetchall()
    
    
    #plt.plot(x_pos, trendline, color='red', linestyle='--')    
    plt.bar(range(len(dataVendor)), [val[1] for val in dataVendor], align='center')
    plt.xticks(range(len(dataVendor)), [val[0] for val in dataVendor]) 
    plt.xticks(rotation=80, fontsize=6)
    plt.ylabel('no. Fradulent Transactions')
    plt.plot()
    plt.show()
        
    
    
    
    
    conn.close()



if __name__ == "__main__":
    plotReports()
