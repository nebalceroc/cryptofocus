from numpy.lib.financial import ipmt
# -*- coding: utf-8 -*-

def pc1(Key):#permutacion 1
    p=[56,48,40,32,24,16,8,0,57,49,41,33,25,17,9,1,58,50,42,
          34,26,18,10,2,59,51,43,35,62,54,46,38,30,22,14,6,61,
          53,45,37,29,21,13,5,60,52,44,36,28,20,12,4,27,19,11,3];
    result = [Key[x] for x in p]
    return "".join(result[:28]) , "".join(result[28:])

def pc2(Key):#permutacion 2
    p= [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,7,15,6,26,
          19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,
          33,52,45,41,49,35,28,31]
    result = [Key[x] for x in p]
            
    return "".join(result)

def ipinv(Key):#permutacion 2
    result = []
    p= [39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,
          30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,
          60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,
          18,58,26,33,1,41,9,49,17,57,25,32,0,40,8,48,
          16,56,24]
    result = [Key[x] for x in p]
            
    return "".join(result)


def calckeys(Key, op):#calcula las llaves
    rot = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    Keys=[]
    #PC-1 permutation
    L, R = pc1(Key)
    #LS 16 veces
    for i in rot:
        L = L[i:] + L[:i]
        R = R[i:] + R[:i]
        Keys.append( pc2(L + R))

    #Diferente a cero si es desencripción
    if (op <> 0):
        Keys.reverse()
   
    return Keys

def ip(msg):#Initial Permutation
    p= [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,
          3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,
          15,7,56,48,40,32,24,16,8,0,58,50,42,34,26,
          18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,
          30,22,14,6]
    result = [msg[x] for x in p] 
            
    return "".join(result)

def e(Key):#expansion e
    p= [31,0,1,2,3,4,3,4,5,6,7,8,7,8,9,10,11,12,11,
          12,13,14,15,16,15,16,17,18,19,20,19,20,21,22,
          23,24,23,24,25,26,27,28,27,28,29,30,31,0]
    result = [Key[x] for x in p] 
            
    return "".join(result)

def permutation(Key):#permutacion del inner
    result = []
    p= [15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,
          1,7,23,13,31,26,2,8,18,12,29,5,21,10,3,24]
    result = [Key[x] for x in p]
    return "".join(result)

def xor(seg1,seg2):#operacion xor
    a = list(seg1)
    b = list(seg2)
    c = ''
    for x in range(len(seg1)):
        if(a[x]==b[x]):
            c+='0'
        else:
            c+='1'

    return c

def stringtobin(msg):#mensaje a binario
    char_arr = [ord(w) for w in msg]
    bin_arr = []
    message = ''
    segment_size = 64
    for c in char_arr:
        bin_arr.append('0'+bin(c)[2:])
        message+='0'+bin(c)[2:]
    amount = 0;
    if(len(message) % segment_size != 0):
        amount = segment_size-(len(message) % segment_size)
    
    if (amount != 0):    
        for x in range(amount):
            message+='0'
    return message

def split_string(string, length):#dividir en segmentos un string
    return [string[i:i+length] for i in range(0, len(string), length)]

def round(message,key):#cada iteracion de las 16

    l = message[0:32]
    r = message[32:]
    li = (xor(l,inner(r,key)))
    result = r + li
    return result

def sbox(index,segment):#sbox de operacion f
    y = int(segment[0]+segment[5],2)
    x = int(segment[1:5],2)
    s = [
        [
            [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
        [
            [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
        [
            [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
        [
            [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
        [
            [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
        [
            [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
            [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
        [
            [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
        [
            [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]]
    
    result = intToBinary(s[index][y][x],4)
    
    return result

def intToBinary(num,size):
    binary = bin(num)
    binary = binary[2:]
            
    if len(binary) <= size:
        for i in range(size-len(binary)):
            binary = "0"+binary;
    else:
        binary = binary[len(binary)-size:]
    return binary

def inner(r,k):#inner function
    a = e(r)
    b = xor(a,k)
    c = split_string(b, 6)
    d = "";
    for i in range(8):
        d += sbox(i, c[i])
    return permutation(d)

def cifrado(message,key,opc):
    ciphersegments=[]
    binkey = stringtobin(key)
    if (opc ==0):   
        msg = stringtobin(message)
    else :
        msg = hextobin(message)
        binkey = key
    msgs = split_string(msg, 64)

    keys = calckeys(binkey, opc)
    for i in msgs:
         cipher = ip(i)
         for j in range(16):
             cipher = round(cipher, keys[j])
         cipher = cipher[32:]+cipher[:32]
         print cipher
         ciphersegments.append(ipinv(cipher))
    #print ciphersegments
    return "".join(ciphersegments)

def hexfin(msg):
    a = split_string(msg, 8)
    b = []
    for x in a:
        b.append(hex(int(x,2))[2:])
    return b
    
def bintostr(msg):
    a = split_string(msg, 8)
    b = []
    cypher_list = []
    for segment in a:
        dec = 0;
        for x in range(len(segment)):
            pot=int(segment[x])*(2**(7-x))
            dec= dec + pot
        cypher_list.append(chr(dec))
    return cypher_list  

def hextobin(msg):
    a = split_string(msg,2)
    result = [] 
    num_of_bits = 8
    for i in a:
        result.append(bin(int(i, 16))[2:].zfill(num_of_bits))
        
    return "".join(result)


#parametros para encripcion
message = "WINTERFELLCOMING"
key = "CIFRADOS"
#parametros para desencripcion
msgdes = "528CCD3A0BEC04166AB34E9B33AF976A"
keybin = hextobin("3130353638343633")


opc = 0 #0 si es desencriptacion, uno si es encriptado
if (opc == 0):
    msg = cifrado(message, key,opc)
    texto_cifrado=hexfin(msg)
else:
    msg = cifrado(msgdes, keybin,opc)
    texto_cifrado=bintostr(msg)



print texto_cifrado
      