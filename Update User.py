import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from datetime import datetime
date = datetime.now()

calabrio_api_user = "username here"
calabrio_api_pass = "password here"


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

s
def basic_user_search(sessionId):
    user_details = {}
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/permission/ViewOrg', headers=header, verify=False)
    for user in get.json():
        ad_login = user['adLogin']
        active = user['active']
        id = user['personId']
        displayId = user['displayId']
        firstName = user['firstName']
        lastName = user['lastName']
        if user['email'] is None:
            continue
        else:
            email = user['email'].lower()
        if email == useremail.lower():
            user_details['ad_login'] = ad_login
            user_details['active'] = active
            user_details['id'] = id
            user_details['displayId'] = displayId
            user_details['firstName'] = firstName
            user_details['lastName'] =  lastName
            user_details['email'] = email 
            return user_details
    return 'not found'


def update_user(sessionId, user_details):
    body = {"groupId": int(team number), 
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "adLogin": displayId,
            "acdId": None,
            "acdServerId": None,
            "roles": [{"id": int(role number),
                       "label": "role name",
                       "name": "role name",
                       "isAgentDefault": False,
                       "isAdminDefault": False,
                       "isSupervisorDefault": False}],
            "scope": {"tenant": None,
                      "groups": [list of associated int(parent groups)],
                      "teams": [list of associated int(team numbers)]},
            "views": [],
            "qmViews": [],
            "isSynchronized": False,
            "isReconcileOnly": False,
            "locale": "en",
            ## uncomment below to activate or deactivate user
            #"deactivated": int(date.timestamp()* 1000)
            #"activated": int(date.timestamp() * 1000)
            }
    print(body)
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    try:
        post = requests.put('https://calabrio.domain_here.com/api/rest/org/common/person/{}'.format(id), headers=header, json=body, verify=False)
        print(post.status_code)
        print(post.text)
        build_output = post.json()

    except Exception as e:
        print(e)
        end_session(sessionId)
        exit()

session = start_session()
user = basic_user_search(session)
if user != 'not found':
    update_user = update_user(session, user)
else:
    print('User not found')
    
end_session(session)