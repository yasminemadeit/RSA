import codecs
import random
from sympy import randprime

def computeGCD(x, y):
    small = min(x,y)
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
    
    
'''
Computing private key for chosen p,q,e
'''
def KeyGeneration():
    p ,q, publicKey,privateKey =2,2,2,0#0,0, 0,0 #need convert hex...

    #while  (not is_prime(p) or not is_prime(q) or p == q ) :
    #    p = random.randint(2,1000)
    #    q = random.randint(2,1000)
        #print(is_prime(p), is_prime(q))
    
    #p = F7E75FDC469067FFDC4E847C51F452DF 
    #q = E85CED54AF57E53E092113E62F436F4F 
    
    p = randprime(100,500)
    q =randprime (501,999)
   
    n=p*q
    EulerPhi = (p-1) *(q-1)#EulerPhi(n) = (p-1) (q-1)
    
    
    while (computeGCD(publicKey,EulerPhi) != 1): #find gcd (e, Euler )= 1 
        publicKey = random.randint(2,1000)
        #print(computeGCD(publicKey,EulerPhi) )
        
    
    #e = 0D88C3
      
    
    #exhaustive search for d/private key 
    #Looking for d when d*e mod phi(n) =1. And d != e. 
    
    for i in range(1,EulerPhi): #(1,9999):
        if (publicKey*i ) %EulerPhi ==1 and publicKey!=i:
            privateKey = i
            break
    
    print("p,q,n,EulerPhi,publicKey,privateKey\n",p,q,n,EulerPhi,publicKey,privateKey,"\n") #debug
   
    return  publicKey,privateKey,n
 


def OLDKeyGeneration():
    publicKey,privateKey =0,0 #e,d #hex values
    
    #need convert hex...
   
    p ,q= 2,7  
    #p ,q= 3,11 
   
    #p = F7E75FDC469067FFDC4E847C51F452DF 
    #q = E85CED54AF57E53E092113E62F436F4F 
   
    
    n=p*q
    EulerPhi = (p-1) *(q-1)#EulerPhi(n) = (p-1) (q-1)
    
   
    publicKey = 5 
    #publicKey = 3
    #e = 0D88C3
      
    
    #exhaustive search for d/private key 
    #Looking for d when d*e mod phi(n) =1. And d != e. 
    
    for i in range(1,1000):
        if (publicKey*i ) %EulerPhi ==1 and publicKey!=i:
            privateKey = i
            break
    
    print("p,q,n,EulerPhi,publicKey,privateKey\n",p,q,n,EulerPhi,publicKey,privateKey,"\n") #debug
   
    return  publicKey,privateKey,n


'''
Compute the cipher text using the plain text and the public key.
'''
def Encryption (message,publicKey,n):
    #cipherText = ""
     
    #convert string x to hex.? #eg x is "2" or x is "a"
    
    #print(bytes(x,'utf-8').hex()) ?
    #if message.isdigit(): #x is "2"
    
    
    # x = 2 -> y = 4 for  eg
    #cipherText = (int(message)**publicKey ) % n #int() works for num input... but not letters...
    listA = []
    for i in message:
        xStr = i.encode('utf-8')
        y=xStr.hex()
        listA.append(y)
    
    cipherText = []
    for i in listA:
        c=((int(i,16))**publicKey)%n
        cipherText.append(c)
    
    return cipherText



'''
Compute the plain text using the cipher text and the private key.
'''
def Decryption (message,privateKey,n):
    plainText = " "
    txt = message.split(",")
    #y = 4 -> x = 2 for  eg
    #plainText = (int(message)**privateKey ) % n
    for i in txt:
        d=( int(i)**privateKey)%n
        d_hex = hex(d)[2:]
        d_bytes =bytes(d_hex,encoding = 'utf-8')
        d_string = codecs.decode(d_bytes,"hex")
        z=(str(d_string,'utf-8'))
        plainText+=z
    return plainText

def Main():
    output = -1
    
    publicKey,privateKey,n = KeyGeneration() #generate keys 
    
    #encrypt and/or decrypt #with same p,q,e values
    choice= -1
    while choice != 0:
        choice = int(input("Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: "))
        
        if choice ==0:
            break
        
        elif choice ==1:
            message = input("Enter plain text: ")
            output = Encryption(message,publicKey,n)
            
            print("Plain text: ", message, "\nEncryption is:", output)
            
        elif choice ==2:
            message = input("Enter cipher text: ")
            output = Decryption(message,privateKey,n)
            print("Cipher text: ", message, "\nDecryption:", output)
        
       
        else:
            print("INVALID")

        print("\n")


def convertPrac(): #possible approach - to try?
    
    
    #hex to str
    import codecs
    y="4120746f702073656372657421"
    y_bytes =bytes(y,encoding = 'utf-8')
    y_string = codecs.decode(y_bytes,"hex")
    x=(str(y_string,'utf-8'))
    print(x)
    
    
    
    #str to hex
    x= "A top secret!"
    xStr = x.encode('utf-8')
    y=xStr.hex()
    print(y)
    
Main()
