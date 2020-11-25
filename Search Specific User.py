import urllib3
import requests

calabrio_api_user = "username here"
calabrio_api_pass = "password here"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
useremail = 'user1@domain_here.com'

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


def basic_user_search(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/permission/ViewOrg', headers=header, verify=False)
    for user in get.json():
        print(user)
        if user['email'] is None:
            continue
        else:
            email = user['email'].lower()
        id = user['personId']
        if email == useremail.lower():
            print(user)
            return id
    return 'not found'

def specific_user_search(sessionId, id):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get(f'https://calabrio.domain_here.com/api/rest/org/common/person/{id}', headers=header, verify=False)
    print(get.json())

session = start_session()
id = basic_user_search(session)
if id != 'not found':
    specific_user_search(session, id)
else:
    print('User not found')
end_session(session)
