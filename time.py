N=int(input())
hora=0
minuto=0
while N>=3600:
    N = N-3600
    hora = (hora +1)
while N<3600 and N>=60:
        N = N-60
        minuto = (minuto+1)
print(str(hora) + ":" + str(minuto) + ":" + str(N))
