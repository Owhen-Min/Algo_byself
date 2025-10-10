def solution(user_id, banned_id):
    l = len(banned_id)
    def possible_group(user):
        nonlocal banned_id, l
        l2 = len(user)
        ls = []
        for i in range(l):
            banned = banned_id[i]
            if len(banned) != l2:
                continue
            if all(banned[j] == user[j] or banned[j] == "*" for j in range(l2)):
                ls.append(i)
        
        return ls
    
    poss_groups = list(poss for poss in map(possible_group, user_id) if poss)
    # [[0,1],[0],[1],[2,3],[2,3]]
    l3 = len(poss_groups)
    
    from collections import deque
    
    q = deque([[]])
    while q:
        curr = q.popleft()
        target = len(curr)
        if target == l:
            ans = set(q)
            ans.add(curr)
            break
        
        for k in range(l3):
            if target in poss_groups[k] and k not in curr:
                q.append(frozenset(list(curr)+[k]))
        
    return len(ans)