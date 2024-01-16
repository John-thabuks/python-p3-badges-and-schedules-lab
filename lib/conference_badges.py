def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names ]

    # l = []    
    # l = []
    # for name in names:
    #     l.append(f"Hello, my name is {name}.")
    # return l


def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index}!"for index, name in enumerate(names, 1)]
    # rooms 1 - 7
        # start at 1
    # list of speakers
        # assign each speaker to each room in rooms list
    # rooms = []
    # for index, name in enumerate(names, 1):
    #     rooms.append(f"Hello, {name}! You'll be assigned to room {index}!")         
    # return rooms

def printer(names):
    b = batch_badge_creator(names)
    for batch in b:
        print(batch)
    assign = assign_rooms(names)
    for rooms in assign:
        print(rooms)
    # return None
