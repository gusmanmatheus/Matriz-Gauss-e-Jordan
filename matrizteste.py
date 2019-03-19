import numpy as np

leitura=open("in.txt",'r')
file_data = leitura.read()
teste = file_data.split("\n")
c=[]
e=0

for d in teste:
 c.insert(e,teste[e].split(" "))
 e=e+1

r= np.array(c)
r =np.array( r, dtype=np.float)

v=[]
s=np.shape(r)

            
print(s)


i = 0
j = 0
n=s[0]-1
m=s[1]-1

while (i <= n and j <= m):
    k = i;
    while (k <= n and r[k][j] == 0):
        k=k+1
			
    if (k <= n):
				
        if (k != i):
            aux=r[k]
            r[k]=r[i]
            r[i]=r[k]
            print(r)

        if (r[i][j] != 1):
            r[i]=r[i]/r[i][j]
            print(r)
        lin=s[0]-1
        colu=s[1]-1
        cont=0
        while (cont <= lin):
            if (cont != i and r[cont][j] != 0):
                contIn=j+1
                print(j)
                while (contIn <= colu):
                    r[cont][contIn] -= r[cont][j] * r[i][contIn]
                    contIn=contIn+1
                r[cont][j] = 0
            cont=cont+1   
        print(r)
        i=i+1
    j=j+1
		
print(r.size)
print(r.itemsize)
print(r[0,3]+r[0,3])
print(r.dtype)
