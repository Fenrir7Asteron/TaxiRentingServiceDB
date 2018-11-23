"""
Main module of the project
"""

from sshtunnel import SSHTunnelForwarder
import MySQLdb as mdb
from sql_interaction_methods import send_sql_query
from config import _remote_host, _ssh_port, _username, _key_path, \
_key_password, _local_port, _remote_port, _db_user, _db_password, _db_name

# You can write queries ONLY INSIDE the with .. as scope. Out of it there is no SSH tunnel!
with SSHTunnelForwarder(
         (_remote_host, _ssh_port),
         ssh_username = _username,
         ssh_pkey = _key_path,
         ssh_private_key_password = _key_password,
         local_bind_address = ('127.0.0.1', _local_port),
         remote_bind_address = ('127.0.0.1', _remote_port)
         ) as server:
    
    conn = None
    conn = mdb.connect(user=_db_user,passwd=_db_password,db=_db_name,host='127.0.0.1',port=_local_port)
    cur = conn.cursor()
    print(conn)
    print(send_sql_query("SELECT * FROM car", conn))
    print(send_sql_query("SELECT * FROM some_table", conn))