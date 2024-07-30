import requests
import os
import datetime

API_BASE_URL = "https://eobras.am.gov.br/obrasgov-map-backend/source/seinfra/contract/"

# We don't have a list of the valid ids. With manual trial and error, I assume
# that there is no id above this number
# The front end doesn't contain these ids
MAX_ID_NUMBER = 20

now = datetime.datetime.now().isoformat()
json_dir = f"json_{now}"
os.mkdir(json_dir)

for id in range(1,MAX_ID_NUMBER):
    id = str(id)
    response = requests.get(API_BASE_URL + id)
    if response.ok:
        with open(f"{json_dir}/{id}.json", 'wb') as file:
            file.write(response.content)
    else:
        print(f"ID {id} does not exist")





