import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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


def parent_group(sessionId):
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/group/permission/ViewOrg', headers=header, verify=False)
    print(get.text)
    for group in get.json():
        print(group['groupId'], group['name'])

session = start_session()
group = parent_group(session)
end_session(session)
