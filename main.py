import datetime
import json
from uuid import uuid4
from pathlib import Path

my_db = {}
selected_db = ""
current_db = ""

ADD_ROW_IN_TABLE = "add"  # add table val1,val2
DEL_ROW_IN_TABLE = "del"  # del table unique_id
GET_TABLE = "get"  # get table *  || get table unique_id
MAKE_TABLE = "make"  # make table_name val1,val2

SELECT_DB = "change"  # change dbname
SHOW_DB = SHOW_TABLE = "show"  # show db | show * table
CREATE_DB = "create_db"  # create_db dbname

SHOW_PARAMETER_DB = "db"

commands_available_table = [
    ADD_ROW_IN_TABLE,
    DEL_ROW_IN_TABLE,
    GET_TABLE,
    MAKE_TABLE,
    SHOW_TABLE
]

commands_available_db = [
    CREATE_DB,
    SELECT_DB,
    SHOW_DB,
]


def is_json(my_json):
    try:
        json_object = json.loads(my_json)
    except ValueError as e:
        return False
    return True


def write_dict_to_file():
    open('keyfile.txt', 'w').close()
    try:
        geeky_file = open('keyfile.txt', 'wt')
        geeky_file.write(str(my_db))
        geeky_file.close()
    except:
        print("Unable to write to file")


def read_db():
    global my_db
    if Path("keyfile.txt").exists():
        inf = open('keyfile.txt', 'r')
        my_db = eval(inf.read())
        inf.close()


def check_if_table_command_valid(val):
    if val in commands_available_table:
        return True
    return False


def check_if_db_command_valid(val):
    if val in commands_available_db:
        return True
    return False


def generate_unique_id():
    return datetime.datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())


def del_row(table_name, id):
    if table_name not in current_db.keys():
        print("table not found")
    elif id not in current_db[table_name]['value'][0]:
        print("Row id not found")
    else:
        del current_db[table_name]['value'][0][id]


def add_row(table_name, rows):
    if table_name not in current_db.keys():
        print("table not found")
    elif len(current_db[table_name]['cols']) >= len(rows):

        current_db[table_name]['value'].append({generate_unique_id(): rows})
    else:
        print("not enough col to save")


def create_table(param, columns):
    retrieve_col = {'cols': columns.split(','),
                    'value': []}
    if param in current_db.keys():
        print("table already exist")
    else:
        current_db[param] = retrieve_col
        print(param + " is created")


def print_tables():
    for i, k in my_db.items():
        if i == selected_db:
            for t, table in k.items():
                print(t)


# Press the green button in the gutter to run the script.
def print_table_data(param):
    global current_db
    current_db = my_db[selected_db]
    if param[1] not in current_db.keys():
        print("table not found " + param[1])
    else:
        if param[2] == '*':
            print(current_db[param[1]])
        elif param[2] in current_db[param[1]]['value'][0]:
            print(current_db[param[1]]['value'][0][param[2]])
        else:
            print('id not found')


def exec_table_command(command_val):
    if selected_db == "":
        print("Please select a Database")
    else:
        if command_val[0] == MAKE_TABLE:
            create_table(command_val[1], command_val[2])
        elif command_val[0] == SHOW_TABLE and command_val[1] == '*' and command_val[2] == 'table':
            print_tables()
        elif command_val[0] == GET_TABLE:
            print_table_data(command_val)
        elif command_val[0] == ADD_ROW_IN_TABLE:
            add_row(command_val[1], command_val[2].split(','))
        elif command_val[0] == DEL_ROW_IN_TABLE:
            del_row(command_val[1], command_val[2])


def print_database():
    for i, k in my_db.items():
        print(i)


def create_db():
    if command_val[1] in my_db:
        print("database already exist")
    else:
        my_db[command_val[1]] = {}
        print(command_val[1] + " created")


def show_database(param):
    global selected_db
    global current_db
    for i, k in my_db.items():
        if i == param:
            selected_db = i
            current_db = my_db[selected_db]
            print(i + " is selected")
    if selected_db == "":
        print("database not found")


def exec_db_command(command_val):
    if command_val[0] == CREATE_DB:
        create_db()
    elif command_val[0] == SHOW_DB and command_val[1] == SHOW_PARAMETER_DB:
        print_database()
    elif command_val[0] == SELECT_DB:
        show_database(command_val[1])


if __name__ == '__main__':
    read_db()
    print('write a command!')
    while True:
        command = input()
        if command == "exit":
            print("Thank for using")
            break
        command_val = command.split()
        if len(command_val) == 3 and check_if_table_command_valid(command_val[0]):
            exec_table_command(command_val)
            write_dict_to_file()
        elif len(command_val) == 2 and check_if_db_command_valid(command_val[0]):
            exec_db_command(command_val)
            write_dict_to_file()
        else:
            print("Invalid command ")
