overview = {"user1": 1, "user2": 2, "user3": "hello"}
data = {1: "Nie znam", 2: "kto to", "hello": "to ten"}

dict1={}

i=0
for item in overview.values():
    i = i + 1
    j = 0
    #print(f'{item} iteracja {i-1}')
    for item2 in data.keys():
        j = j + 1
        #print(f'{item2} iteracja {j-1}')
        if item == item2:
            #print(f'{item} == {item2}')
            #print(f'i{i-1} == j{j-1}')
            print(f'{list(overview.keys())[i-1]} == {list(data.values())[j-1]}')
            dict1[list(overview.keys())[i-1]]=list(data.values())[j-1]

print(dict1)
print(f' wprowadz swojego uzytkownika z {dict1}')
wybor=input()
print(dict1[wybor])