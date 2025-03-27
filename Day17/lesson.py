class User:
    #Constructor / Initialization --> Executed every time a Class instance is created
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0 #Default value
        self.following = 0
        print("New user is being created...")
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(id = '001', username = 'Daniel')

print(user_1.username)
print(f"Followers: {user_1.followers}")

user_2 = User('002', "Alejandro")
user_1.follow(user = user_2)

print(f"User {user_1.id} - Followers: {user_1.followers}  Following: {user_1.following}")
print(f"User {user_2.id} - Followers: {user_2.followers}  Following: {user_2.following}")