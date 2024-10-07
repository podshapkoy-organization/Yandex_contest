c = int(input())
cities = {}

for _ in range(c):
    city_name, room_count = input().split()
    room_count = int(room_count)
    cities[city_name] = []

    for _ in range(room_count):
        schedule, room_name = input().split()
        cities[city_name].append((schedule, room_name))
m = int(input())
for _ in range(m):
    query = input().split()
    l = int(query[0])
    req_cities = query[1:]
    found = False
    for hour in range(24):
        select_rooms = []
        possible = True
        for city in req_cities:
            found_room = False
            for schedule, room_name in cities[city]:
                if schedule[hour] == '.':
                    select_rooms.append(room_name)
                    found_room = True
                    break
            if not found_room:
                possible = False
                break
        if possible:
            print("Yes", " ".join(select_rooms))
            found = True
            break
    if not found:
        print("No")
