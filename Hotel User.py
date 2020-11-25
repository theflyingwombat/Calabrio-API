import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def end_session(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    end = requests.delete('https://calabrio.domain_here.com/api/rest/authorize', headers=header, verify=False)
    if end.status_code == 200:
        print('Session Successfully Ended')
    else:
        print('Session Failed to End')


def start_session():
    data = {"userId": "apiuser@domain_here.com",
            "password": "L0ves0520pwd",
            "language": "en"}
    output = requests.post('https://calabrio.domain_here.com/api/rest/authorize', json=data, verify=False)
    sessionId = output.json()['sessionId']
    print("SessionID: " + sessionId)
    return sessionId


def build_hotel_user(session, firstName, lastName, email, displayName):
    body = {"firstName": firstName,
            "lastName": lastName,
            "email": email,
            "displayName": displayName,
            "parentGroup": int(parent group number),
            "groupId": int(group number),
            "timeZone": "America/Chicago",
            "isSynchronized": False,
            "isReconcileOnly": False,
            "adLogin": None,
            "isSystemUser": False,
            'roles': [{'id': int(role number), 'label': 'Role Name', 'name': 'Role Name', 'isAgentDefault': False, 'isAdminDefault': False, 'isSupervisorDefault': False}],
            'scope': {'tenant': None, 'groups': [], 'teams': []},
            'views': [],
            'qmViews': [],
            'isMerged': False,
            "isHotdeskDefaultUser": True
            }
    header = {"cookie": "hazelcast.sessionId=" + session}
    try:
        get = requests.post('https://calabrio.domain_here.com/api/rest/org/common/person', headers=header, json=body, verify=False)
        output = get.json()
        print(get.text)
        print(get.status_code)
        if get.status_code == 200:
            id = str(output['id'])
            print(f'{displayName} Successfully Built')
            return id
        else:
            print(f'Failed to build {displayName}')
            return 'error'
        print(get.json())
    except Exception as e:
        print(e)
        return 'error'


def update_hotel_user(session, id, firstName, lastName, email, displayName):
    body = {"firstName": firstName,
            "lastName": lastName,
            "email": email,
            "displayName": displayName,
            "parentGroup": int(parent group number),
            "groupId": int(group number),
            "timeZone": "America/Chicago",
            "isSynchronized": False,
            "isReconcileOnly": False,
            "adLogin": None,
            "isSystemUser": False,
            'roles': [{'id': int(role number), 'label': 'Role Name', 'name': 'Role Name', 'isAgentDefault': False, 'isAdminDefault': False, 'isSupervisorDefault': False}],
            'scope': {'tenant': None, 'groups': [], 'teams': []},
            'views': [],
            'qmViews': [],
            'isMerged': False,
            "isHotdeskDefaultUser": True}
    header = {"cookie": "hazelcast.sessionId=" + session}
    try:
        post = requests.put('https://calabrio.domain_here.com/api/rest/org/common/person/{}'.format(id), headers=header, json=body, verify=False)
        print(post.status_code)
        if post.status_code == 200:
            print(f'{displayName} Successfully Built')
        else:
            print(f'Failed to build {displayName}')
        print(post.json())
    except Exception as e:
        print(e)


firstName = 'User First Name'
lastName = 'User First Name'
displayName = 'User First Last'
email = 'User Email'
session = start_session()
print(session)
id = build_hotel_user(session, firstName, lastName, email, displayName)
if id == 'error':
    print('User not built, Stopping')
else:
    update = update_hotel_user(session, id, firstName, lastName, email, displayName)
end_session(session)
