def solution(k, room_number):
    answer = []
    rooms = dict()
    
    for room in room_number:
        if room not in rooms:
            rooms[room] = room+1
        else:
            visited = [room]
            while room in rooms:
                room = rooms[room]
                visited.append(room)
            
            for trace in visited:
                rooms[trace] = room+1
                
        answer.append(room)
    return answer