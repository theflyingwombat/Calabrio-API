import requests
import urllib3
from ldap3 import Server, Connection, ALL
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


'''
This script pulls info from LDAP, you can accomplish the same thing by manually entering the info in to Build_User
'''

username = 'Username to search'

'''
GET LDAP USER INFO
'''
ad_username = 'username here'
ad_pass = 'password here'
ad_user = 'domain_here\\' + ad_username
searchbase = 'dc=domain_here,dc=com'
ad_server = 'ldap_server.domain_here.com'


calabrio_api_user = "username here"
calabrio_api_pass = "password here"
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

def ldap_user_search(username):
    searchfilter = '(sAMAccountName=' + username + ')'
    attrs = ['givenName', 'sn', 'mail', 'displayName']

    # initiate LDAP Connection
    server = Server(ad_server, get_info=ALL)
    with Connection(server, user=ad_user, password=ad_pass, auto_bind=True) as conn:

        # locate user by saml name
        conn.search(searchbase, searchfilter, attributes=attrs)
        user_result = conn.entries
        if user_result == []:
            result = ('No AD account found for user: ' + username)
            return result
        json_result = user_result[0].entry_to_json()
        print(user_result[0].entry_to_json())
        return (json_result)

'''
User Search
'''
full_login = 'domain_here\\' + username.lower()
# print(full_login)
header = {"cookie": "hazelcast.sessionId=" + sessionId}
get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/permission/ViewOrg', headers=header, verify=False)
# print(get.json())
for user in get.json():
    ad_login = user['adLogin']
    active = user['active']
    id = user['personId']
    # print(ad_login, active)

    if ad_login is not None and full_login == ad_login.lower():
        print(user)
        print('USER FOUND - ' + ad_login)
        break
        
 def basic_user_search(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/permission/ViewOrg', headers=header, verify=False)
    for user in get.json():
        ad_login = user['adLogin']
        if ad_login is not None and full_login == ad_login.lower():
            print(user)
            print('USER FOUND - ' + ad_login)
            return 'user found'
        return 'no user found'


def build_user(sessionId, firstName, lastName, email, displayName)
    body = {"firstName": firstName,
            "lastName": lastName,
            "email": email,
            "displayName": displayName,
            "enabledForSchedule": False,
            "timeZone": "America/Chicago",
            "acdId": "",
            "acdServerId": None
            }
    print(body)
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    try:
        get = requests.post('https://calabrio.domain_here.com/api/rest/org/common/person', headers=header, json=body, verify=False)
        return get.json()
    except Exception as e:
        return get.json()


session = start_session()
id = basic_user_search(session)
ldap_user = ldap_user_search(username)
ldap_user = json.loads(ldap_user)
'''
Grab Attributes
'''
firstName = ldap_user['attributes']['givenName'][0]
lastName = ldap_user['attributes']['sn'][0]
displayName = ldap_user['attributes']['displayName'][0]
email = ldap_user['attributes']['mail'][0]
user_search = basic_user_search(session)
if session == 'user found':
    print('user found - ending script')
    exit()
else:
    build = build_user(session, firstName, lastName, email, displayName)
    print(build)

end_session(session)