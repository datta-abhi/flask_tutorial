# creating db to store user data
import json
class Database:
    def insert(self,name,email,password):

        # for reading existing json content
        with open('users.json','r') as rf:
            users = json.load(rf)

    # check if user already exists
        if email in users:
            return 0
        else:
            users[email] = [name, password]

        with open('users.json','w') as wf:
            json.dump(users,wf,indent=3)
            return 1