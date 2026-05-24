import requests
import time

recommendations_url = "http://127.0.0.1:8000"
features_store_url = "http://127.0.0.1:8010"
events_store_url = "http://127.0.0.1:8020"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

user_id = 1291248
event_item_ids = [41899, 102868, 5472, 5907]

for event_item_id in event_item_ids:
    resp = requests.post(events_store_url + "/put", 
                         headers=headers, 
                         params={"user_id": user_id, "item_id": event_item_id})

time.sleep(1)

params = {"user_id": user_id, 'k': 5}

resp = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
online_recs = resp.json()

print(online_recs)