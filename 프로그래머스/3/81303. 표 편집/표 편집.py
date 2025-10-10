def solution(n, k, cmd):
    stack = []
    next = {i: i+1 for i in range(n)}
    prev = {i: i-1 for i in range(n)}
    next[n-1] = -1
    
    for c in cmd:
        cm = c[0]
        
        if cm == "D":
            for _ in range(int(c[2:])):
                k = next[k]
        elif cm == "U":
            for _ in range(int(c[2:])):
                k = prev[k]
        elif cm == "C":
            stack.append(k)
            prev[next[k]] = prev[k]
            next[prev[k]] = next[k]
            k = next[k] if next[k] != -1 else prev[k]
        else:
            i = stack.pop()
            prev[next[i]] = i
            next[prev[i]] = i
    ls = ["O"]*n
    for i in stack: ls[i] = "X"
    return "".join(ls)