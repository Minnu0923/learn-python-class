from pymongo import MongoClient # type: ignore
#establish connection
client = MongoClient('mongodb://localhost:27017/')
db = client['6PM']
user_col=db['Users']

users=user_col.find()

for user in users:
    print(user['uid'], user['uname'])
