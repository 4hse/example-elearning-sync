import requests
import uuid 
import env

#current user access token
authentication = {'access-token': env.access_token}
person_id = "7fa46f5d-fabe-4979-b923-2bb88224cf80"
action_id = "de5e9431-caf2-4e5b-a4b2-9318021558c2"

#create certificate
certificate_id = uuid.uuid1()
certificate = {
  'certificate_id': certificate_id,
  'validity_unit': 'YEAR',
  'validity': 3,
  'date_release': '2022-01-10',
  'date_expire': '2025-01-10',
  'name': 'Formazione anticendio rischio alto',
  'action_type': 'TRAINING',
  'resource_id': person_id,
  'tenant_id': env.project_id
}
r = requests.post('https://service.4hse.com/v2/certificate/create', data=certificate, params=authentication)
print(r.text)

#create certificate_action
certificate_action = {
  'certificate_action_id': uuid.uuid1(),
  'certificate_id': certificate_id,
  'action_id': action_id,
  'tenant_id': env.project_id
}
r = requests.post('https://service.4hse.com/v2/certificate-action/create', data=certificate_action, params=authentication)
print(r.text)