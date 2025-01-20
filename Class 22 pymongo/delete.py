from pymongo import MongoClient # type: ignore
#establish connection
client = MongoClient('mongodb://localhost:27017/')
db = client['6PM']
user_col=db['Users']

#delete one document

status=user_col.delete_one({'uid':1})
print(status)
print("Deleted successfully")