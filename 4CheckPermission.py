
def check_permissions(user, permission):
    if user == "admin":
        permission == "zapis" or "odczytanie" or "modyfiy"
        print("Permission accempt")
    elif user == "super":
        permission == "modyfiy" or "odczytanie"
        print("Permission accempt")
    elif user == "standard":
        permission == "odczytanie"
        print("Permission accempt")
    elif user == "peasant":
        print("You can nothing")
    else:
        print('premission denied')


print('Wprowadz rodzaj użytkownika "Admin, Super, Standard, Peasant "')
user=input().lower()

print('Wprowadz co użytkownik chce zrobić: zapis , odczytanie, modyfiy')
permission=input().lower()

check_permissions(user,permission)


