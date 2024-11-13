def solution(m, musicinfos):
    m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    answer = ''
    ls =[]
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(',')
        lastingtime = int(musicinfo[1][:2])*60+int(musicinfo[1][3:]) - int(musicinfo[0][:2])*60-int(musicinfo[0][3:])
        ls.append([lastingtime] + musicinfo[2:])
    n_ls = [0] * len(ls)
    for i in range(len(n_ls)):
        n_ls[i] = ls[i][2] * (ls[i][0]//len(ls[i][2])) + ls[i][2][:ls[i][0]%len(ls[i][2])]
    print(n_ls)
    return answer