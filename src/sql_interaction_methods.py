"""
Module containing methods for simplifying database interaction
"""

import MySQLdb

def connect_to_DB (ip, login, password, db_name):
    __fname__ = 'connect_to_DB'
    
    try:
        conn = MySQLdb.connect(host=ip, user=login, 
                               passwd=password, db=db_name)
    except MySQLdb.Error as err:
        conn.close()
        
        return {'response': 'Connection error: {}'.format(err), 'status': 'error'}
    
    return {'response': conn, 'status': 'OK', 'error': 'None'}

def send_sql_query (sql, conn):
    __fname__ = 'send_sql_query'
    
    data = None
    
    try:
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        data = cur.fetchall()
        
        conn.commit()
    except MySQLdb.Error as err:
        return {'response': 'Query error: {}'.format(err), 'status': 'error'}

    return {'response': data, 'status': 'OK'}