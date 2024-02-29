import requests
import env

#retrieve the list of action subscriptions
params = {'filter[tenant_id]': env.project_id, 'access-token': env.access_token}

r = requests.get('https://service.4hse.com/v2/action-subscription/index', params=params)
print(r.text)