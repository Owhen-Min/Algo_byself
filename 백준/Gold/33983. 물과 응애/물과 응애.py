n = int(input())

ho_counter = 0
h_counter = 0
hoh_counter = 0
if not n%3:
    for char in input():
        if char == "H":
            if ho_counter:
                ho_counter -=1
                hoh_counter += 1
            else: h_counter += 1
        elif char == "O":
            if h_counter:
                ho_counter +=1
                h_counter -= 1
            else:
                if hoh_counter:
                    hoh_counter -= 1
                    ho_counter += 2
                else:
                    print("mix")
                    break
    else:
        if h_counter or ho_counter:
            print("mix")
        else: print("pure")
else: print("mix")