import urllib3
import requests

calabrio_api_user = "username here"
calabrio_api_pass = "password here"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
useremail = 'User1@domain_here.com'

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

def user_status(sessionId, id):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/{}/status'.format(id), headers=header, verify=False)
    print(get.json()
    status = get.json()['status']
    return status

def user_lock(sessionId, id):
    data = {"status":"unlocked"}
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.put('https://calabrio.domain_here.com/api/rest/org/common/person/{}/status'.format(id), headers=header, json=data, verify=False)
    print(get.status_code)
    # status code:400
    #{"errorMessage":"User's account is already unlocked","requestId":"12345"}
    print(get.json())



session = start_session()
id = basic_user_search(session)
if id != 'not found':
    specific_user_search(session, id)
else:
    print('User not found')
status = user_status(session,id)
if status == 'locked':
    unlock = user_lock(session, id)
else:
    print('User not locked')
end_session(session)