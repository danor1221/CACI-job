# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:46:26 2022

@author: danor
"""

import sqlite3, time

from generateTables import generate_tables

# Unhash the below line to generate the tables in the database file SQLDatabase.db. This should
# not be necessary unless the database is empty. If so, run this line once.
#generate_tables()

def sanitise():
    conn = sqlite3.connect('SQLDatabase6.db')
    cur = conn.cursor()
    
    
    cur.execute("""delete from fraud
                where credit_card_number not like '5018%'
                and credit_card_number not like '5020%'
                and credit_card_number not like '5038%'
                and credit_card_number not like '56%'
                and credit_card_number not like '51%'
                and credit_card_number not like '52%'
                and credit_card_number not like '54%'
                and credit_card_number not like '55%'
                and credit_card_number not like '222%'
                and credit_card_number not like '4%'
                and credit_card_number not like '34%'
                and credit_card_number not like '37%'
                and credit_card_number not like '6011%'
                and credit_card_number not like '65%'
                and credit_card_number not like '300%'
                and credit_card_number not like '301%'
                and credit_card_number not like '304%'
                and credit_card_number not like '305%'
                and credit_card_number not like '36%'
                and credit_card_number not like '38%'
                and credit_card_number not like '35%'
                and credit_card_number not like '2131%'
                and credit_card_number not like '1800%';       
                """)
    
    cur.execute("""delete from transaction001
                where credit_card_number not like '5018%'
                and credit_card_number not like '5020%'
                and credit_card_number not like '5038%'
                and credit_card_number not like '56%'
                and credit_card_number not like '51%'
                and credit_card_number not like '52%'
                and credit_card_number not like '54%'
                and credit_card_number not like '55%'
                and credit_card_number not like '222%'
                and credit_card_number not like '4%'
                and credit_card_number not like '34%'
                and credit_card_number not like '37%'
                and credit_card_number not like '6011%'
                and credit_card_number not like '65%'
                and credit_card_number not like '300%'
                and credit_card_number not like '301%'
                and credit_card_number not like '304%'
                and credit_card_number not like '305%'
                and credit_card_number not like '36%'
                and credit_card_number not like '38%'
                and credit_card_number not like '35%'
                and credit_card_number not like '2131%'
                and credit_card_number not like '1800%';
                """)
    
    cur.execute("""delete from transaction002
                where credit_card_number not like '5018%'
                and credit_card_number not like '5020%'
                and credit_card_number not like '5038%'
                and credit_card_number not like '56%'
                and credit_card_number not like '51%'
                and credit_card_number not like '52%'
                and credit_card_number not like '54%'
                and credit_card_number not like '55%'
                and credit_card_number not like '222%'
                and credit_card_number not like '4%'
                and credit_card_number not like '34%'
                and credit_card_number not like '37%'
                and credit_card_number not like '6011%'
                and credit_card_number not like '65%'
                and credit_card_number not like '300%'
                and credit_card_number not like '301%'
                and credit_card_number not like '304%'
                and credit_card_number not like '305%'
                and credit_card_number not like '36%'
                and credit_card_number not like '38%'
                and credit_card_number not like '35%'
                and credit_card_number not like '2131%'
                and credit_card_number not like '1800%';
                """)    
    
    
    cur.execute("""alter table transaction002
                add vendor VARCHAR(10);        
                """)
    time.sleep(1)
    
    cur.execute("""update transaction002
                set vendor = 'maestro'
                where credit_card_number like '5018%'
                or credit_card_number like '5020%'
                or credit_card_number like '5038%'
                or credit_card_number like '56%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'mastercard'
                where credit_card_number like '51%'
                or credit_card_number like '52%'
                or credit_card_number like '54%'
                or credit_card_number like '55%'
                or credit_card_number like '222%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'visa'
                where credit_card_number like '4%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'amex'
                where credit_card_number like '34%'
                or credit_card_number like '37%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'discover'
                where credit_card_number like '6011%'
                or credit_card_number like '65%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'diners'
                where credit_card_number like '300%'
                or credit_card_number like '301%'
                or credit_card_number like '304%'
                or credit_card_number like '305%'
                or credit_card_number like '36%'
                or credit_card_number like '38%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'jcb16'
                where credit_card_number like '35%';
                """)
    time.sleep(1)
    cur.execute("""update transaction002
                set vendor = 'jcb15'
                where credit_card_number like '2131%'
                or credit_card_number like '1800%';
                """)
    time.sleep(1)
    
    
    
    conn.commit()
    conn.close()



if __name__ == "__main__":
    sanitise()


