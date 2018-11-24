from generator import quotate, get_name, get_email, get_phone_number,\
    get_address, get_username, get_password, get_bank_account, get_rating,\
    get_schedule, get_integer, get_double, get_string, get_color, get_model,\
    get_material, get_shape, get_event, get_order_id, get_repair_id,\
    get_provision_id, parse_datetime, adjust_datetime
    
from random import randint
from sql_interaction_methods import send_sql_query

def get_user():
    full_name = get_name()
    e_mail = quotate(get_email(full_name))
    full_name = quotate(full_name)
    phone_number = quotate(get_phone_number())
    location_of_residence = quotate(get_address())
    username = quotate(get_username())
    password_hash = quotate(str(hash(get_password())))
    bank_account = quotate(get_bank_account())
    
    query = "INSERT INTO `user`(`full_name`, `e-mail`, `phone_number`, \
    `location_of_residence`, `username`, `password_hash`, `bank_account`) \
    VALUES (%s,%s,%s,%s,%s,%s,%s)" % (full_name, e_mail, phone_number, location_of_residence, username, password_hash, bank_account)
    
    return query

def get_customer(user_id):
    customer_id = user_id;
    rating = quotate(str(get_rating()))
    #family_members = get_family_members()
    
    return "INSERT INTO `customer`(`customer_id`, `rating`) \
    VALUES (%d,%s)" % (customer_id, rating)
    """
    for member in family_members:
        member = quotate(member)
        queries.append("INSERT INTO `customer_family_members`(`customer_id`, \
        `family_member`) VALUES (%d,%s)" % (customer_id, member))
    """

def get_worker(user_id):
    worker_id = user_id;
    salary = randint(30000, 100000) // 1000 * 1000
    working_schedule = quotate(get_schedule());
    
    return "INSERT INTO `worker`(`worker_id`, `salary`, `working_schedule`) \
    VALUES (%d,%d,%s)" % (worker_id, salary, working_schedule)

def get_battery():
    charge_level = get_integer(0, 100) # percentage
    maximal_charge = get_double(18, 48) #kW*h
    
    return "INSERT INTO `battery`(`charge_level`, `maximal_charge`) \
    VALUES (%d,%d)" % (charge_level, maximal_charge)

def get_car_model():
    name = quotate(get_model())
    producing_year = get_integer(2012, 2018)
    comfort_level = get_integer(0, 9)
    
    return "INSERT INTO `model`(`name`, `producing_year`, `comfort_level`) \
    VALUES (%s,%d,%d)" % (name, producing_year, comfort_level)

def get_car(model_id, battery_id):
    license_plate = quotate(get_string(7).upper())
    insurance_id = quotate(str(get_integer(1000000000, 9999999999)))
    print(insurance_id)
    color = quotate(get_color())
    smoking_is_allowed = get_integer(0, 1)
    
    return "INSERT INTO `car`(`license_plate`, `model_id`, `battery_id`, \
    `insurance_id`, `color`, `is_smoking_allowed`) VALUES (%s,%d,%d,%s,%s,%d)" \
    % (license_plate, model_id, battery_id, insurance_id, color, smoking_is_allowed)


def get_part_type(model_id):
    name = quotate(get_string(6, 12))
    material = quotate(get_material())
    weight = get_double(0.01, 100)
    size = get_double(0.001, 10)
    
    return "INSERT INTO `part_type`(`model_id`, `name`, `material`, `weight`, \
    `size`) VALUES (%d,%s,%s,%f,%f)" \
    % (model_id, name, material, weight, size)
    
def get_part(part_type_id):
    color = quotate(get_color())
    part_condition = quotate(get_string(4, 12))
    
    return "INSERT INTO `part`(`part_type_id`, `color`, `part_condition`) \
    VALUES (%d,%s,%s)" % (part_type_id, color, part_condition)

def get_workshop():
    address = quotate(get_address())
    return "INSERT INTO `workshop`(`address`) VALUES (%s)" % (address)

def get_parts_at_workshop_storage(workshop_id, part_id):
    return "INSERT INTO `parts_at_workshop_storage`(`workshop_id`, `part_id`) \
    VALUES (%d,%d)" % (workshop_id, part_id)
    
def get_charge_station():
    address = quotate(get_address())
    price_of_charging = get_integer(600, 1500)
    
    return "INSERT INTO `charge_station`(`location`, \
    `price_of_charging_per_hour`) VALUES (%s,%f)" % (address, price_of_charging)

def get_socket(station_id):
    plug_shape = quotate(get_shape())
    return "INSERT INTO `socket`(`station_id`, `plug_shape`) \
    VALUES (%d,%s)" % (station_id, plug_shape)

def get_odometer_reading(license_plate):
    license_plate = quotate(license_plate)
    at_order_time = get_integer(0, 999999)
    at_pickup_point = at_order_time + get_integer(1, 150)
    at_destination_point = at_pickup_point + get_integer(1, 500)
    
    return "INSERT INTO `odometer_readings`(`car_license_plate`, \
    `at_order_time`, `at_pickup_point`, `at_destination_point`) \
    VALUES (%s,%f,%f,%f)" % (license_plate, at_order_time, at_pickup_point, 
                           at_destination_point)

def insert_car_availability(license_plate):
    license_plate = quotate(license_plate)
    is_available = 1
    return "INSERT INTO `car_availability`(`license_plate`, `available`) \
    VALUES (%s,%d)" % (license_plate, is_available)

def get_provider(worker_id):
    return "INSERT INTO `provider`(`provider_id`) VALUES (%d)" % (worker_id)

def get_event_query(datetime, conn):
    time = parse_datetime(datetime)
    event = get_event()
    queries = []
    if event == 'order_made':
        customer_id = get_integer(10000, 11411)
        number_of_passengers = get_integer(1, 4)
        luggage_presence = get_integer(0, 1)
        queries.append("INSERT INTO `order`(`customer_id`, `number_of_passengers`, \
        `luggage_presence`) VALUES (%d,%d,%d)" % (customer_id, number_of_passengers, 
                                                  luggage_presence))
        
        order_id = get_order_id()
        pickup_point = quotate(get_address())
        destination_point = quotate(get_address())
        
        print(order_id)
        
        cost = get_integer(200, 1000)
        queries.append("INSERT INTO `order_data`(`order_id`, `pickup_point`, \
        `destination_point`, `time_of_order`, `cost`) VALUES (%d,%s,%s,%s,%d)" % 
        (order_id, pickup_point, destination_point, time, cost))
        
        queries.append("INSERT INTO `order_status`(`order_id`, `status`) \
        VALUES (%d,%s)" % (order_id, "'pending'"))
    elif event == 'car_assigned':
        order_id = send_sql_query("SELECT `order_id` FROM `order_status` WHERE `status`='pending'", conn)
        print(order_id)
        if (order_id['status'] != 'OK' or len(order_id['response']) == 0):
            return queries
        
        number = len(order_id['response'])
        order_id = order_id['response'][get_integer(0, number - 1)]['order_id']
        available_car = send_sql_query("SELECT `license_plate` \
        FROM `car_availability` WHERE `available`=1", conn)
        
        print(available_car)
        
        if (available_car['status'] != 'OK' or len(available_car['response']) == 0):
            return queries
        
        number = len(available_car['response'])
        assigned_car = available_car['response'][get_integer(0, number - 1)]['license_plate']
        assigned_car = quotate(assigned_car)
        queries.append("INSERT INTO `car_assigned_to_order`(`order_id`, \
            `assigned_car`) VALUES (%d,%s)" % (order_id, assigned_car))
        
        queries.append("UPDATE `order_status` SET `status`=%s \
        WHERE `order_id`=%d" % ("'car_is_assigned'", order_id))
        
        queries.append("UPDATE `car_availability` SET `available`=0 \
        WHERE `license_plate`=%s" % (assigned_car))
    elif event == 'reached_pickup':
        order_id = send_sql_query("SELECT `order_id` FROM `order_status` WHERE `status`='car_is_assigned'", conn)
        print(order_id)
        if (order_id['status'] != 'OK' or len(order_id['response']) == 0):
            return queries
        
        number = len(order_id['response'])
        order_id = order_id['response'][get_integer(0, number - 1)]['order_id']

        queries.append("UPDATE `order_data` SET `time_of_reaching_pickup_point`=%s \
        WHERE `order_id`=%d" % (time, order_id))

        queries.append("UPDATE `order_status` SET `status`=%s \
        WHERE `order_id`=%d" % ("'car_reached_pickup_point'", order_id))
    elif event == 'reached_destination':
        order_id = send_sql_query("SELECT `order_id` FROM `order_status` WHERE `status`='car_reached_pickup_point'", conn)
        print(order_id)
        if (order_id['status'] != 'OK' or len(order_id['response']) == 0):
            return queries
        
        number = len(order_id['response'])
        order_id = order_id['response'][get_integer(0, number - 1)]['order_id']

        queries.append("UPDATE `order_data` SET `time_of_reaching_destination_point`=%s \
        WHERE `order_id`=%d" % (time, order_id))

        queries.append("UPDATE `order_status` SET `status`=%s \
        WHERE `order_id`=%d" % ("'completed'", order_id))
        
        license_plate = send_sql_query("SELECT `assigned_car` \
        FROM `car_assigned_to_order` WHERE `order_id`=%d" % (order_id), conn)
        
        print(license_plate)
        
        if (license_plate['status'] != 'OK' or len(license_plate['response']) == 0):
            return queries
        
        number = len(license_plate['response'])
        license_plate = license_plate['response'][get_integer(0, number - 1)]['assigned_car']
        queries.append(get_odometer_reading(license_plate))
        
        license_plate = quotate(license_plate)
        queries.append("UPDATE `car_availability` SET `available`=1 \
        WHERE `license_plate`=%s" % (license_plate))
    elif event == 'check':
        workshop_id = get_integer(1, 5)
        available_car = send_sql_query("SELECT `license_plate` \
        FROM `car_availability` WHERE `available`=1", conn)
        
        if (available_car['status'] != 'OK' or len(available_car['response']) == 0):
            return queries
        
        number = len(available_car['response'])
        license_plate = available_car['response'][get_integer(0, number - 1)]['license_plate']
        license_plate = quotate(license_plate)
        cost = get_integer(400, 600)
        
        queries.append("INSERT INTO `maitenance_check`(`workshop_id`, \
        `car_license_plate`, `work_cost`, `date_of_check`) \
        VALUES (%d,%s,%d,%s)" % (workshop_id, license_plate, cost, time))
    elif event == 'repair':
        workshop_id = get_integer(1, 5)
        available_car = send_sql_query("SELECT `license_plate` \
        FROM `car_availability` WHERE `available`=1", conn)
        
        if (available_car['status'] != 'OK' or len(available_car['response']) == 0):
            return queries
        
        number = len(available_car['response'])
        license_plate = available_car['response'][get_integer(0, number - 1)]['license_plate']
        license_plate = quotate(license_plate)
        cost = get_integer(1000, 20000)
        
        queries.append("INSERT INTO `repair`(`workshop_id`, \
        `car_license_plate`, `work_cost`, `date_of_check`) \
        VALUES (%d,%s,%d,%s)" % (workshop_id, license_plate, cost, time))
        
        available_parts = send_sql_query("SELECT `part_id` \
        FROM `parts_at_workshop_storage` WHERE `workshop_id`=%d" \
        % (workshop_id), conn)
        
        if (available_parts['status'] != 'OK' or len(available_parts['response']) == 0):
            return queries
        
        number = len(available_parts['response'])
        disposable = get_integer(1, min(number, 5))
        repair_id = get_repair_id()
        for i in range(disposable):
            part_id = available_parts['response'][i]['part_id']
            queries.append("INSERT INTO `parts_used_in_repair`(`repair_id`, `part_id`) \
            VALUES (%d,%d)" % (repair_id, part_id))
            
            queries.append("DELETE FROM `parts_at_workshop_storage` \
            WHERE `workshop_id`=%d AND `part_id`=%d" % (workshop_id, part_id))
    elif event == 'provision':
        provider_id = get_integer(9901, 9910)
        workshop_id = get_integer(1, 5)
        
        queries.append("INSERT INTO `provision`(`provider_id`, \
        `workshop_id`, `date_of_provision`) \
        VALUES (%d,%d,%s)" % (provider_id, workshop_id, time))
        
        number_of_provided_parts = get_integer(10, 50)
        provision_id = get_provision_id()
        for i in range(number_of_provided_parts):
            part_id = get_integer(1, 500)
            queries.append("INSERT INTO `provided_parts`(`provision_id`, \
            `part_id`) VALUES (%d,%d)" % (provision_id, part_id))
            queries.append("INSERT INTO `parts_at_workshop_storage`(`workshop_id`, \
            `part_id`) VALUES (%d,%d)" % (workshop_id, part_id))
    elif event == 'recharge':
        finish_time = adjust_datetime(datetime, get_integer(300, 1800))
        finish_time = parse_datetime(finish_time)
        battery_id = get_integer(1, 50)
        station_id = get_integer(1, 20)
        
        queries.append("INSERT INTO `recharge`(`start_time`, `finish_time`, \
        `battery_id`, `station_id`) VALUES (%s,%s,%d,%d)" % (time, finish_time, 
                                                             battery_id, station_id))
        
        queries.append("UPDATE `battery` SET `charge_level`=100 \
        WHERE `battery_id`=%d" % (battery_id))
        
    return queries

#print(get_odometer_reading(get_string(7)))
#print(get_worker(1))
#print(get_battery())
#print(get_car(250, 100))
#print(get_car_model())
#print(get_part_type(4))