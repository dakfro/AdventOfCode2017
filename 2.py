from itertools import combinations as co
t = []#.........................................Lines 2-6 store the input data into array t
for i in open("input2.txt").readlines():#.......
    t.append(i.strip("\n"))#....................
for i in range(len(t)):#........................
    t[i] = [int(j) for j in t[i].split("\t")]#..
r1,r2 = sum(max(i) - min(i) for i in t),0
for k in t:
    for j1 in co(k,2):
        i,j = sorted(j1)[0],sorted(j1)[1]
        if j%i == 0:
            r2 += j//i
            break# not necessary, but decreases speed a little
print(str(r1) + "\n" + str(r2))
