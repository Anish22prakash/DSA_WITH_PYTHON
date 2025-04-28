class YouTube :
    def __init__(self,username,subscribers = 0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def subscribe(self, user):
        self.subscribers += 1
        user.subscriptions += 1

user1 = YouTube("Anish")
user2 = YouTube("Rohan")
user3 = YouTube("Mohit")

user1.subscribe(user2)
print(user1.__dict__)
user2.subscribe(user1)
user1.subscribe(user3)
print(user1.__dict__)

print(f"subscription of user 1 {user1.subscriptions}")
print(f"subscription of user 2 {user2.subscriptions}")
print(f"subscription of user 3 {user3.subscriptions}")
        