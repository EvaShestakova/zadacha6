try:
    f = open("data.txt")
except:
    print("cannot open file")
    exit()
flag = 0
fl=0
k = 0
n = 0
a = 0
z = 0
for line in f:
    for i in line.split():
        flag=1
        a = int(i)
        if a>=0:
            fl=1
        if (a<0 and z==0) or (a<0 and z<0 and a>z):
            z=a
        if k+a>0:
            k=k+a
        else:
            k=0
        if k>n:
            n=k
if flag == 0:
    print("empty file")
else:
    if fl==1:
        print(n)
    else:
        print(z)
f.close()
