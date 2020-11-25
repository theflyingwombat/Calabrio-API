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



def teams(sessionId):
    #group and team are interchangable names in API
    header = {"cookie": "hazelcast.sessionId=" + sessionId}
    get = requests.get('https://calabrio.domain_here.com/api/rest/org/common/team/permission/ViewOrg', headers=header, verify=False)
    print(get.text)
    for group in get.json():
        #will print all groups and associated parent group
        print(group['parentGroupId'], '-', group['groupId'], group['name'])


session = start_session()
teams = teams(session)
end_session(session)
