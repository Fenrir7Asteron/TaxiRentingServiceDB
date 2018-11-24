from random import randint as rand
from random import uniform
from random import choice
from datetime import datetime
import string


men_firstnames = ['Barret', 'Berry', 'Cecil', 'Damon', 'Ellis', 'Gilbert', 
                  'Harold', 'Irvine', 'Jarred', 'Jaymes', 'Kyle', 'Kris', 
                  'Mike', 'Normand', 'Ode']

women_firstnames = ['Gretta', 'Rubye', 'Myrle', 'Adelina', 'Aleesha', 'Alexia', 
              'Alisha', 'Anne', 'Aria', 'Carina', 'Catherine', 'Cindi', 'Debi', 
              'Eden', 'Eveline', 'Fay', 'Frieda', 'Gwendolyn', 'Gwenevere', 
              'Jennifer', 'Jill', 'Lena', 'Lily', 'Olive']

lastnames = ['Steiner', 'Gruber', 'Huber', 'Bauer', 'Wagner', 'Pichler', 
             'Moser', 'Mayer', 'Rossi', 'Russo', 'Bruno', 'Hansen', 'Johansen', 
             'Olsen', 'Larsen', 'Andersen', 'Nilsen', 'Silva', 'Santos', 
             'Melnyk', 'Shevchenko', 'Boyko']

mail_services = ['gmail.com', 'yandex.ru', 'ya.ru', 'mail.ru', 'rambler.ru', 
                 'yahoo.com', 'inbox.com']

cities = ['Ankara', 'Athens', 'Baltimore', 'Barcelona', 'Berlin', 'Bogotá', 
    'Chicago', 'Dublin', 'Helsinki', 'London', 'Madrid', 'Osaka', 'Paris', 
    'Rome', 'Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 
    'Kazan', 'Innopolis', 'Krasnoyarsk', 'Omsk', 'Perm', 'Barnaul', 'Tomsk', 
    'Vladivostok', 'Ryazan']

# Any correlations with actual San Andreas streets are pure coincidences
streets = ['6th Street', 'Auto Circle', 'Broadway', 'Dix Road', 'Fifth Avenue', 
           'Grove Street', 'Harry Gold Parkway', 'Hasselhoff Street', 
           'Interstate 45', 'Julius Thruway', 'Las Venturas Boulevard', 
           'Main Street', 'Market Boulevard', 'Mulholland Drive', 
           'Old Venturas Strip', 'Saints Boulevard', 'San Fierro Scenic Road']

usernames1 = ['4meandthi', 'Admiradom', 'AirCart', 'Alertsteric', 'Aliment', 
             'Amgustam', 'Aortami', 'BauerReptile', 'Beastargium', 'BillSelf', 
             'BinderSee', 'Biologi', 'Blackencess', 'Blondievely', 
             'BroadwayAngelic', 'Bromorks', 'Cakentelia', 'CandyWavesMon', 
             'ChellGazette', 'Chronicleup', 'Chunkyouet', 'CistKlug', 
             'Clartorg', 'Comicones', 'Contentecut', 'Corphole', 'Crossoria', 
             'Malthiso', 'Mediumerat', 'MellowKit', 'MessageSosa', 'Mofferlist', 
             'Momentech', 'MonGamerKat', 'Monsterca', 'NoteDarkFace', 
             'NoteSumo', 'Nyctankview', 'Pacelthe', 'Penguings', 'Pitypell']

usernames2 = ['Conspiracy', 'Covenkle', 'Dagenera', 'Donstest', 'Dronusedal', 
              'Enjoyerie', 'Equentum', 'ExtraRosesAngel', 'Ezstorv', 
              'Freakeronge', 'FunThenorn', 'Gambitrice', 'Gigglyphar', 
              'Goofyrellak', 'GoWeblogTins', 'Greyeprico', 'Helloft', 
              'Holydatens', 'Inebayer', 'Inikrine', 'Interiorne', 'JeanUpdates', 
              'Jillered', 'Joyougheenr', 'JungRacing', 'JuzTrickyDeck', 
              'Kaasani', 'KittyFamous', 'Larkatel', 'Laurenic', 'LawFun', 
              'LedgerAway', 'LetterIffy', 'Louislogi', 'Manesoft', 'ManiakNotice']

special_symbols = ['!', '?', '$', '&', '*', '-', '_', '+', '/', '<', '>', '|']

emoji = ['(⁎˃ᆺ˂)', '(҂⌣̀_⌣́)', '(๑･`▱´･๑)', 'ლ(ಠ_ಠლ)', '(ᗒᗩᗕ)՞', '(♥ω♥*)', 
         'Ꮚ^ꈊ^Ꮚ', 'ᏊᵋꈊᵋᏊ', '₍₍ (ง ˙ω˙)ว ⁾⁾', '(๑•́ ω •̀๑)', '(●///▽///●)', 
         'ღゝ◡╹)ノ♡', '(灬♥ω♥灬)', '彡ﾟ◉ω◉ )つー☆*', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', '(=ↀωↀ=)', 
         '(ㅇㅅㅇ❀)', '(^･ｪ･^)']

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

color = ['black', 'white', 'red', 'blue', 'yellow', 'silver', 'green', 'orange', 
         'grey', 'purple', 'midnight blue', 'gold', 'brown', 'pink', 
         'metallic red', 'metallic blue', 'grabber blue', 'hot pink', 
         'dark green', 'magenta']

model = ['BMW i3', 'BMW Brilliance Zinoro 1E', 'Bolloré Bluecar', 'BYD e6', 
         'Chery QQ3 EV', 'Chevrolet Bolt EV', 'Citroën C-Zero', 'COURB C-ZEN', 
         'ElectraMeccanica Solo', 'Fiat 500e', 'Ford Focus Electric', 
         'Girfalco Azkarra', 'Honda Fit EV', 'Hyundai Ioniq Electric', 
         'Hyundai Kona Electric', 'JAC J3 EV', 'Jaguar I-Pace', 'Kewet Buddy', 
         'Kia Soul EV', 'Lightning GT', 'Mahindra e2o plus', 'Nissan Leaf']

material = ['adamantite', 'alluminium', 'steel', 'carbon', 'iron', 'titanium', 
            'silver', 'gold', 'bronze', 'silicon', 'wood', 'magnesium', 'copper']

shape = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

events = ['order_made', 'order_made', 'order_made', 'car_assigned', 'car_assigned', 
          'car_assigned', 'reached_pickup', 'reached_pickup', 'reached_destination', 
          'reached_destination', 'recharge', 'recharge', 'provision', 'check', 'repair']

order_id = 29
repair_id = 12
provision_id = 12

def get_name(): 
    gender = rand(0, 1)
    if (gender == 0): # male
        firstname = choice(men_firstnames)
    else:
        firstname = choice(women_firstnames)
        
    lastname = choice(lastnames)
    return firstname + ' ' + lastname

def get_email(fullname):
    space_index = fullname.find(' ')
    e_mail = fullname[0].lower() + '.' + fullname[space_index + 1:].lower() + \
        '@' + choice(mail_services)
    return e_mail

def get_phone_number():
    return '+7' + str(rand(1000000000, 9999999999))

def get_address():
    return str(rand(1, 319)) + ', ' + choice(streets) + ', ' + choice(cities)

def get_username():
    number_presence = rand(0, 3)
    special_symbol_presence = rand(0, 5)
    emoji_presence = rand(0, 7)
    username = choice(usernames1) + choice(usernames2)
    
    if (number_presence == 3):
        number = str(rand(10, 9999))
        index = rand(0, len(username))
        username = username[:index] + number + username[index:]
    if (special_symbol_presence == 5):
        special_symbol = choice(special_symbols)
        index = rand(0, len(username))
        username = username[:index] + special_symbol + username[index:]
    if (emoji_presence == 7):
        username += choice(emoji)
        
    return username

def get_password():
    length = rand(6, 24)
    password = ""
    for i in range(length):
        password += choice(string.ascii_letters)
    return password

def get_bank_account():
    account = ""
    for i in range(16):
        account += choice(string.digits)
    return account

def get_rating():
    return round(uniform(0.0, 5.0), 2)

def get_family_members():
    size = rand(0, 4)
    members = []
    for i in range(size):
        members.append(get_name())
        
    return members

def quotate(string):
    return "'" + string + "'"

def get_current_datetime():
    return datetime.utcnow()

def parse_datetime(datetime):
    date = str(datetime)
    return quotate(date[:date.find('.')])

def adjust_datetime(datetime, seconds):
    return datetime.fromtimestamp(datetime.timestamp() + seconds)

def get_schedule():
    weekend_size = rand(2, 4)
    schedule_is_normal = rand(0, 4) != 4
    
    result = ""
    if schedule_is_normal:
        starting_day = rand(0, 6)
        ending_day = rand(starting_day, 6)
        result = days[starting_day] + '-' + \
        days[ending_day] + ', '
    else:
        n = 7
        for day in days:
            n = n - 1 
            if rand(0, 1) == 0 and weekend_size > 0:
                weekend_size = weekend_size - 1
            elif n - weekend_size >= 0:
                result += day + ', '
            else:
                weekend_size = weekend_size - 1
    
    starting_time = rand(8, 12)
    workday_length = rand(6, 8)
    result += str(starting_time) + ':00-' + \
    str(starting_time + workday_length) + ':00'
    
    return result
    
def get_integer(low, high):
    return rand(low, high)

def get_double(low, high):
    return uniform(low, high)

def get_string(low, high = 0):
    if high == 0:
        low, high = high, low
        
    result = ""
    for i in range(low, high):
        if rand(0, 1) == 0:
            result += choice(string.ascii_letters)
        else:
            result += choice(string.digits)
            
    return result

def get_color():
    return choice(color)

def get_model():
    return choice(model)

def get_material():
    return choice(material)

def get_shape():
    return choice(shape)

def get_event():
    return choice(events)

def get_order_id():
    global order_id
    order_id = order_id + 1
    return order_id

def get_repair_id():
    global repair_id
    repair_id = repair_id + 1
    return repair_id

def get_provision_id():
    global provision_id
    provision_id = provision_id + 1
    return provision_id

#print(get_string(7))
#print(get_string(1, 4))
#print(get_color())
#print(get_schedule())
#print(get_username())
"""
name = get_name();
print(name)
print(get_email(name))
print(get_phone_number())
print(get_address())
print(get_username())
password = get_password()
print(password)
print(hash(password))
print(get_rating())
print(get_family_members())
"""
