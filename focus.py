class Focus():
    key=[]    
    def __init__(self,key):
        self.key=key
        
    def cypherSegment(self, segment):              
        entrada=list(segment)
        salida = []
        for i in range(len(entrada)):
            salida.append(entrada[i])
            
        for x in range(len(segment)):
            data=entrada[x]
            for y in range(len(segment)):
                if(self.key[y]-1==x):
                    salida[y]=data
        
        salida_entera=''
        for char in salida:
            salida_entera+=char                
        return salida_entera