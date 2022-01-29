import datetime, calendar, jwt
from helpers.constants import SECRET_HERE as secret, algo

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhc3lhIiwicm9sZSI6InVzZXIiLCJleHAiOjE2NTQ2MzczOTd9.FGDbjDh_-o0s4uQEU2hb2-Zc6nkRc1lcM1W-XJQNczM"

data = {
  "id": 1,
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhc3lhIiwicm9sZSI6InVzZXIiLCJleHAiOjE2NDM0MDkwODF9.wNzKpg_viFogXpxODQHfX0GujRuK-wfEO_8Z0NQZbr4",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InZhc3lhIiwicm9sZSI6InVzZXIiLCJleHAiOjE2NTQ2MzkyODF9.wdAuuxFRbDSRvMmGTBNDV9PePtaY53yITlc80pBb4sQ"
}

def data_(**kwargs):
    print(kwargs['id'])

data_(id=1,access_token=2)