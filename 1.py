t = []
for i in open("input1.txt").readlines():
    t.append(i.strip("\n"))
t = t[0]
r1,r2 = 0,0
for i in range(len(t)):
    if t[i] == t[(i+1)%len(t)]:
        r1 += int(t[i])
    if t[i] == t[(i+len(t)//2)%len(t)]:
        r2 += int(t[i])
print(str(r1) + "\n" + str(r2))
