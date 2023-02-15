class User:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def introduce(self,guest_name):
        print("Hello {}! Contact me at {} .".format(guest_name,self.email))



anand = User("reachanand","Anand Verma", "averma8@umd.edu")
bulbul = User("bulbul","Bulbul Verma", "bulbul@umd.edu")
champ = User("champ","Champ Steve", "champ@umd.edu")
Fin = User("fin","Fin Rogers", "Fin@umd.edu")
Siddharth = User("sidd","Siddharth Ajmera", "Siddharth@umd.edu")
tarun = User("tarun3","Tharun Reddy", "tarun@umd.edu")
vikas = User("vikky","Vikas Patidar", "vikas@umd.edu")


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self,user):
        i = 0
        while i < len(self.users):
            if(self.users[i].username > user.username):
                break
            i+=1
        self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user


    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

database = UserDatabase()
database.insert(anand)
database.insert(Siddharth)
database.insert(bulbul)


users = database.list_all()

for u in users:
    print(u.username)


database.update(User(username="reachanand",name="Anand",email="anandverma55@gmail.com"))

users = database.list_all()

for u in users:
    print(u.name)