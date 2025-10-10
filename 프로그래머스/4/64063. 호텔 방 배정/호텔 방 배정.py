import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    rooms = dict()
    
    def find_rooms(room):
        if room not in rooms:
            rooms[room] = room+1
            return room
        
        empty = find_rooms(rooms[room])
        rooms[room] = empty+1
        
        return empty
    
    return list(map(find_rooms,room_number))