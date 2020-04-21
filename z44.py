f = open("data.txt")
flag = 0
k = 0
n = 0
a = 0
for line in f:
    for i in line.split():
        a = int(i)
        if flag == 0:
            n = a
            if a>0:
                k=a
            flag = 1
        else:
            if a<0:
                if a>n:
                    n=a
                k=0
            elif a==0:
                if a>n:
                    n=a
            elif a>0:
                k=k+a
                if k>n:
                    n=k
if flag == 0:
    print("empty file")
else:
    print(n)
f.close()
