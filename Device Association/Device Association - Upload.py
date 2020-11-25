import urllib3
import requests

calabrio_api_user = "username here"
calabrio_api_pass = "password here"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def start_session():
    data = {"userId": calabrio_api_user,
            "password": calabrio_api_pass,
            "language": "en"}
    output = requests.post('https://calabrio.domain_here.com/api/rest/authorize', json=data, verify=False)
    sessionId = output.json()['sessionId']
    print("Calabrio SessionID: " + sessionId)
    return sessionId


def end_session(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    end = requests.delete('https://calabrio.domain_here.com/api/rest/authorize', headers=header, verify=False)
    if end.status_code == 200:
        print('Session Successfully Ended')
    else:
        print('Session Failed to End')


def upload_csv(sessionId):
    files = {'file': open(r'C:\folder_path_here\Calabrio API\test.csv', 'rb')}
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    print(files)
    get = requests.post('https://calabrio.domain_here.com/api/rest/fileimport/devices', files=files, headers=header, verify=False)
    print(get.text)
    print(get.status_code)
    print(get.json())

'''
400
{'errorMessage': 'Error in file import, line 2! Error importing device DEVICENAME_HERE. Reason: 400 Cannot assign multiple devices to one person. Inserting Device: DEVICENAME_HERE, Current Device: DEVICENAME_HERE, Person ID: 123..', 'requestId': '12345'}

{'errorMessage': "Error in file import, line 2! Device 'DEVICENAME_HERE' not found associated with Telephony Group 'TELEPHONE_GROUP_HERE'. Confirm this device is configured with this Telephony Group.", 'requestId': '12345'}

{'errorMessage': 'Error in file import! The person, EMAIL_HERE, has duplicate device associations at lines 2 and 3.', 'requestId': '12345'}


200
{'status': 'SUCCESS', 'responseText': 'The file was successfully imported'}
'''

session = start_session()
id = upload_csv(session)
end_session(session)
