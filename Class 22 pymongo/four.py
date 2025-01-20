from pymongo import MongoClient # type: ignore
#establish connection
client = MongoClient('mongodb://localhost:27017/')
db = client['6PM']
user_col=db['Users']

male_users=user_col.find({'gender':'Male'})

for user in male_users:
    print(user['uid'], user['uname'], user['gender'])
