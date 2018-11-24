"""
Main module of the project
"""

from sshtunnel import SSHTunnelForwarder
import MySQLdb as mdb
from sql_interaction_methods import send_sql_query

from config import _remote_host, _ssh_port, _username, _key_path, \
_key_password, _local_port, _remote_port, _db_user, _db_password, _db_name

from generator import get_address, quotate, get_current_datetime, parse_datetime,\
    adjust_datetime, get_name, get_email, get_phone_number, get_username,\
    get_integer, adjust_datetime
from query_constructor import get_user, get_customer, get_worker, get_car_model,\
    get_battery, get_car, get_part_type, get_part, get_workshop,\
    get_parts_at_workshop_storage, get_charge_station, get_socket,\
    get_event_query

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
    conn = mdb.connect(user=_db_user,passwd=_db_password,db=_db_name,host='127.0.0.1',port=_local_port,charset="utf8",use_unicode=True)
    cur = conn.cursor()
    print(conn)
    """
    print(send_sql_query("SELECT * FROM `order`", conn))
    print(send_sql_query("SELECT * FROM `customer`", conn))
    #print(send_sql_query("INSERT INTO `user`(`full_name`, `e-mail`, `phone_number`, `location_of_residence`, `username`, `password_hash`, `bank_account`) VALUES ('Bogdan Fedotov', 'b.fedotov@innopolis.ru', '+79869185046', 'Innopolis', 'kek', 'fgfsad', '1236581738162')", conn))
    #print(send_sql_query("INSERT INTO `customer`(`customer_id`, `rating`) VALUES (1,4,56)", conn))
    #print(send_sql_query("INSERT INTO `order`(`customer_id`, `number_of_passengers`, `luggage_presence`) VALUES (1,2,0)", conn))
    pickup_point = quotate(get_address())
    destination_point = quotate(get_address())
    current_datetime = get_current_datetime()
    date = parse_datetime(current_datetime)
    print(date)
    current_datetime = increase_datetime(current_datetime, 120)
    date = parse_datetime(current_datetime)
    print(date)
    
    #print(send_sql_query("INSERT INTO `order_data`(`order_id`, `pickup_point`, `destination_point`, `time_of_order`, `time_of_reaching_pickup_point`, `time_of_reaching_destination_point`, `cost`) VALUES (2," + pickup_point + "," + destination_point + "," + str(date) + "," + str(date) + "," + str(date) + ", 100)", conn))
    print(send_sql_query("SELECT * FROM `customer`", conn))
    print(send_sql_query("SELECT * FROM `order`", conn))
    print(send_sql_query("SELECT * FROM `order_data`", conn))
    """
    #n = 9901
    #while n <= 9910:
    #    result = send_sql_query(get_provider(n), conn)
    #    if (result['status'] == 'OK'):
    #        n = n + 1
    #        print(n)
    #    else:
    #        print(result)
    
    #for i in range(10000, 11411):
    #    send_sql_query(get_customer(i), conn)
    #    print(i)
    
    #for i in range(9901, 10000):
    #    send_sql_query(get_worker(i), conn)
    #    print(i)


    current_datetime = get_current_datetime()
    current_datetime = adjust_datetime(current_datetime, -31536000)
    n = 1
    while n <= 3000:
        current_datetime = adjust_datetime(current_datetime, get_integer(20, 120))
        queries = get_event_query(current_datetime, conn)
        for query in queries:
            result = send_sql_query(query, conn)
            if (result['status'] == 'OK'):
                n = n + 1
                print(n)
            else:
                print(result)

    
"""
    n = 1
    while n <= 50:
        license_plate = send_sql_query("SELECT `license_plate` FROM `car` \
        WHERE `battery_id`=%d" % n, conn)['response'][0]['license_plate']
        result = send_sql_query(insert_car_availability(license_plate), conn)
        if (result['status'] == 'OK'):
            n = n + 1
            print(n)
        else:
            print(result)
    """