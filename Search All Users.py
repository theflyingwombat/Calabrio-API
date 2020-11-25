import urllib3
import requests

calabrio_api_user = "Username Here"
calabrio_api_pass = "Password Here"
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


def basic_user_search(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/person/permission/ViewOrg', headers=header, verify=False)
    for user in get.json():
        print(user)


session = start_session()
id = basic_user_search(session)
end_session(session)
