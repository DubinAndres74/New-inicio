def imprimir_matriz(matriz):
    
    for fila in matriz: 
        for elemento in fila: 
            print(elemento, end="\t")  
        print() 
        
matriz = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
]

print("matriz generada:") 
imprimir_matriz(matriz)
