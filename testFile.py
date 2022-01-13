# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:52:57 2022

@author: danor
"""

import sqlite3
import getReports
import sanitiser
import unittest


class TestcallQueryNum(unittest.TestCase):
    """
    Test callQueryNum function
    """
    def testExceptionQueryNumError(self):
        query = """
                    select * fom fraud
                """
        
        with self.assertRaises(Exception):
            returnValue = getReports.callQueryNum(query)
    
    def testExceptionQueryAllError(self):
        query = """
                    select * fom fraud
                """
        
        with self.assertRaises(Exception):
            returnValue = getReports.callQueryAll(query)






class TestcallremoveC(unittest.TestCase):
    """
    test removeC function in sanitiser
    """
    def testExceptionremoveC(self):
        table = "faud"
        
        with self.assertRaises(Exception):
            returnValue = sanitiser.removeC(table)
    
    def testRemovesAllDesired(self):
        """
        test removeC function by giving it a table with cards to be removed and
        making sure it removes the desired cards
        """
        conn = sqlite3.connect('SQLDatabase.db')
        cur = conn.cursor()
        
        # create a testtable in the database
        cur.execute("""CREATE TABLE testtableRC (
                credit_card_number BIGINT,
                ipv4 VARCHAR(15),
                state VARCHAR(2)
                );
                """)
    
        cur.execute("""
                    INSERT INTO testtableRC VALUES
                    (98,'192.168.102.7','WA'),
                    (15615622,'192.168.246.102','RI'),
                    (0000000,'192.168.222.52','TX');
                    """)
        
        conn.commit()
        conn.close()
        
        # remove unwanted cards
        sanitiser.removeC("testtableRC")
        
        
        conn = sqlite3.connect('SQLDatabase.db')
        cur = conn.cursor()
        
        # create query to test testtable has no cards left in it
        query = """select * from testtableRC
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
                    """
        cur.execute(query)
        result = cur.fetchall()
        
        # delete testtable
        cur.execute("""
                    drop table testtableRC;
                    """)
    
        conn.commit()
        conn.close()
        
        
        
        # run assertion to prove testtable had all card removed from it
        self.assertTrue(result == [])



class TestcalladdVC(unittest.TestCase):
    """
    test addVC function in sanitiser by checking that it adds the a fourth column
    and then adds the correct values to each row
    """
    def testAddsDesiredColumns(self):
        conn = sqlite3.connect('SQLDatabase.db')
        cur = conn.cursor()
        
        # create a testtable in the database
        cur.execute("""CREATE TABLE testtableVC (
                credit_card_number BIGINT,
                ipv4 VARCHAR(15),
                state VARCHAR(2)
                );
                """)
    
        cur.execute("""
                    INSERT INTO testtableVC VALUES
                    (5018,'192.168.102.7','WA'),
                    (4,'192.168.246.102','RI'),
                    (55,'192.168.222.52','TX'),
                    (301,'10.186.58.92',NULL),
                    (1800,'10.65.191.187','UT'),
                    (35,'10.68.149.54',NULL),
                    (6011,'192.168.216.58',NULL),
                    (34,'10.55.8.196',NULL);
                    """)
        
        conn.commit()
        conn.close()
        
        # Add the columns
        sanitiser.addVC("testtableVC")
        
        
        conn = sqlite3.connect('SQLDatabase.db')
        cur = conn.cursor()
        
        # create query to test testtable has desired columns in it
        query = """select vendor from testtableVC;"""

        cur.execute(query)
        result = cur.fetchall()
        
        # delete testtable
        cur.execute("""
                    drop table testtableVC;
                    """)
    
        conn.commit()
        conn.close()
        
        
        # run assertion to prove testtable had all card removed from it
        desiredResult = [('maestro',), ('visa',), ('mastercard',), ('diners',), ('jcb15',), ('jcb16',), ('discover',), ('amex',)]
        self.assertTrue(result == desiredResult)





if __name__ == "__main__":
    unittest.main()