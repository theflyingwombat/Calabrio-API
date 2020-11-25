import csv

'''
Grab contents of current CSV file
'''
current_file = []
with open(r'C:\folder_path_here\Calabrio API\test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row == []:
            current_file = [['DeviceName', 'DeviceType', 'Extensions', 'VirtualDeviceId', 'VirtualDeviceName', 'TelephonyGroup', 'DisplayID', 'Username', 'DomainName', 'LastName', 'FirstName', 'MonitorServer', 'RecordingCluster', 'RecordingType']]
        else:
            current_file.append(row)
            print(row)

user_list = [{'Type': 'Location_1', 'DeviceName': 'DEVICE_NAME_1', 'Extension': 'Extension_1', 'Email': 'Email_1', 'DomainName': 'Username_1', 'LastName': 'Lastname_1', 'FirstName': 'Firstname_1'},
             {'Type': 'Location_1', 'DeviceName': 'DEVICE_NAME_2', 'Extension': 'Extension_2', 'Email': 'Email_2', 'DomainName': 'Username_2', 'LastName': 'Lastname_2', 'FirstName': 'Firstname_2'},
             {'Type': 'Location_2', 'DeviceName': 'DEVICE_NAME_3', 'Extension': 'Extension_3, Extension_4', 'Email': 'Email_3', 'DomainName': '', 'LastName': 'Lastname_3', 'FirstName': 'Firstname_3'}]
header = ['DeviceName', 'DeviceType', 'Extensions', 'VirtualDeviceId', 'VirtualDeviceName', 'TelephonyGroup', 'DisplayID', 'Username', 'DomainName', 'LastName', 'FirstName', 'MonitorServer', 'RecordingCluster', 'RecordingType']


'''
Grab user list from file and append users to current file.
'''
for user in user_list:
    telephonyGroup = 'CUCM_' + user['Type'] + '_TG'
    recordingCluster = 'CUCM_' + user['Type'] + '_RG'
    if user['Type'] == 'Location_1':
        username = 'domain_here\\' + user['DomainName']
        device = [user['DeviceName'], 'Cisco Phone Device', user['Extension'], 'null', 'null', telephonyGroup, user['DeviceName'], user['Email'], username, user['LastName'], user['FirstName'], '', recordingCluster, 'Network Recording']
        if device in current_file:
            print(user['DeviceName'] + ' already in CSV File')
        current_file.append(device)
    elif user['Type'] == 'Location_2':
        username = ''
        device = [user['DeviceName'], 'Cisco Phone Device', user['Extension'], 'null', 'null', telephonyGroup, user['DeviceName'], user['Email'], username, user['LastName'], user['FirstName'], '', recordingCluster, 'Network Recording']
        if device in current_file:
            print(user['DeviceName'] + ' already in CSV File')
            continue
        current_file.append(device)
print(current_file)

'''
Write users to CSV file
'''
try:
    with open(r'C:\folder_path_here\Calabrio API\test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(current_file)
except Exception as e:
    print(e)
    print('File Open!!')
print('--------------------------------------------')


def erase_csv():
    '''
    Erase CSV and replace with headers
    '''
    changes = [['DeviceName', 'DeviceType', 'Extensions', 'VirtualDeviceId', 'VirtualDeviceName', 'TelephonyGroup', 'DisplayID', 'Username', 'DomainName', 'LastName', 'FirstName', 'MonitorServer', 'RecordingCluster', 'RecordingType']]
    try:
        with open(r'C:\folder_path_here\Calabrio API\test.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(changes)
    except Exception as e:
        print(e)
        print('File Open!!')
    return 'erased'
#print(erase_csv())
