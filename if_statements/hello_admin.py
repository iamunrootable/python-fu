usernames = ['lisa','billy','laura','bob', 'dan', 'admin']
#usernames = []
for username in usernames:
    if username:
        print(f"Hello {username}")
    elif username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
if usernames == []:
    print("We need to find some users!")