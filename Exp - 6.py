# 0 = Dirty, 1 = Clean
room = {'A': 0, 'B': 0}
location = 'A'

print("Initial State:", room)

if room[location] == 0:
    room[location] = 1
    print("Cleaned Room A")

location = 'B'

if room[location] == 0:
    room[location] = 1
    print("Cleaned Room B")

print("Final State:", room)
