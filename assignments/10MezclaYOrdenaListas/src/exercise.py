def main():
    #escribe tu código abajo de esta línea
    L1= []
    while True:
        numero=(input)
        
        if numero == '*':
            break
        L1.append(int(numero))
    
    L2=[]
    while True:
        numero=(input)
        
        if numero=='*':
            break
        L2.append(int(numero))
    
    print('L1=')
    print(L1)

    print('L2=')
    print(L2)

    L3=[]
    L3= L1+L2
    L3.sort()

    print('LORDENADA=')
    print(L3)

if __name__=='__main__':
    main()
