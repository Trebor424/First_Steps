users = [
    {"id": 5, "first_name": "Tomasz", "last_name": "Kozak"},
    {"id": 4, "first_name": "Kamil", "last_name": "Kozak"},
    {"id": 1, "first_name": "Teresa", "last_name": "Kozak"},
    {"id": 2, "first_name": "Adolf", "last_name": "Kozak"},
    {"id": 3, "first_name": "Krzysztof", "last_name": "Kubiak"},
]


print(f"The lenght of dictionray is to {len(users)}")

for user in users:
    print(f"{user}")
for user in users:
    if user.get("id") == 1:
        print(f"The person whose have a id nr 1 is: {user.values()}")
    elif user.get("id") == 3:
        print(f'The person whose have a id nr {user.get("id")} is: {user.values()}')
    elif user.get("id") == 4:
        print(f'The person whose have a id nr {user.get("id")} is: {user.values()}')
    elif user.get("id") == 5:
        print(f'The name of person index number 5 is: {user.get("first_name")}')
