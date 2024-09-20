def solution(numbers, hand):
    answer = ''
    positions = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        0: (3,1)
    }
    curr_l = (3,0)
    curr_r = (3,2)

    for num in numbers:
        if num in [1,4,7]:
            curr_l = positions[num]
            answer += 'L'
        elif num in [3,6,9]:
            curr_r = positions[num]
            answer += 'R'
        else:
            y, x = positions[num]
            dist_r = abs(curr_r[0]-y) + abs(curr_r[1]-x)
            dist_l = abs(curr_l[0]-y) + abs(curr_l[1]-x)
            if dist_r < dist_l:
                curr_r = positions[num]
                answer += 'R'
            elif dist_r == dist_l:
                if hand == 'right':
                    curr_r = positions[num]
                    answer += 'R'
                else:
                    curr_l = positions[num]
                    answer += 'L'
            else:
                curr_l = positions[num]
                answer += 'L'

    return answer



print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))