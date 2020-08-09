import dataset

database = dataset.connect('mssql+pyodbc://sa:p@ssw0rd@localhost:1433/UNO-local?driver=SQL+Server+Native+Client+11.0')
transits = database['UNOTRANS'].all()

def get_table_data(username, password, server, database, table):
    database = dataset.connect('mssql+pyodbc://'+username+':'+password+'@'+server+':1433/'+database+
        '?driver=SQL+Server+Native+Client+11.0')
    # transits = database[table].all()
    # TODO: add where clause for data - don't fetch all the data...
    transits = database.query('SELECT CARDCODE, BT, FC, CC, DATEIO FROM UNOTRANS')
    data_list = []
    for transit in transits:
        data_list.append(transit)

    return data_list


# for transit in transits:
#     print(transit['CARDCODE'], transit['BT'], transit['FC'], transit['CC'], transit['DATEIO'])

local_db_entry = get_table_data("sa","p@ssw0rd","localhost","UNO1","UNOTrans")
local_db_exit  = get_table_data("sa","p@ssw0rd","localhost","UNO2","UNOTrans")
main_db        = get_table_data("sa", "p@ssw0rd","localhost","UNO-local","UNOTRANS")

all_local_data = local_db_entry + local_db_exit

print(type(all_local_data))

# for d in all_local_data:
#     print(d)

for d in main_db:
    print(d)