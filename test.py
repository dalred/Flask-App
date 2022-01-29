import datetime, calendar, jwt
from helpers.constants import SECRET_HERE as secret, algo


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9sZWciLCJyb2xlIjoiYWRtaW4iLCJpZCI6MywiZXhwIjoxNjQzNDcyNjkzfQ.cKTNgXk8Tm_tSpMb4eWSmkNFjjxE8xZNWzQYhBvkbdU'
user = jwt.decode(token, secret, algorithms=[algo])
print(user)