class S_Box():
    key=[]    
    def __init__(self,key):
        self.key=key
        
    def cypherSegment(self, segment):              
        entrada=int(segment,2)
        salida=self.key[entrada]-1

        salida=bin(salida)[2:]

        if (len(salida) % 3 != 0):
            for x in range(3-len(salida)%3):
                salida='0'+salida

                
        return salida