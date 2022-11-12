''' 
eg 1:

p, q, n, EulerPhi, publicKey, privateKey
 367 701 257267 256200 781 40021 

Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 1
Enter plain text: 4
Plain text:  4 
Encryption is: [24604]


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 2
Enter cipher text: 24604
Cipher text:  24604 
Decryption:  4


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 0

----------------

eg2:

p, q, n, EulerPhi, publicKey, privateKey
 401 811 325211 324000 7 185143 

Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 1
Enter plain text: 10
Plain text:  10 
Encryption is: [85303, 46760]


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 2
Enter cipher text: 85303, 46760
Cipher text:  85303, 46760 
Decryption:  10


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 0

-------------------
eg3:

p, q, n, EulerPhi, publicKey, privateKey
 293 659 193087 192136 321 65841 

Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 1
Enter plain text: top secret!! 99*12.
Plain text:  top secret!! 99*12. 
Encryption is: [117208, 57938, 44291, 3662, 121651, 26027, 113178, 167981, 26027, 117208, 21405, 21405, 3662, 3863, 3863, 101293, 10422, 113782, 63550]


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 2
Enter cipher text: 117208, 57938, 44291, 3662, 121651, 26027, 113178, 167981, 26027, 117208, 21405, 21405, 3662, 3863, 3863, 101293, 10422, 113782, 63550
Cipher text:  117208, 57938, 44291, 3662, 121651, 26027, 113178, 167981, 26027, 117208, 21405, 21405, 3662, 3863, 3863, 101293, 10422, 113782, 63550 
Decryption:  top secret!! 99*12.


Enter input. 1 to encrypt, 2 to decrypt, 0 to quit: 0
'''

import codecs
import random
from sympy import randprime

def computeGCD(x, y): #gcd (e, EulerPhi )
    gcd = 0 
    small = min(x,y)
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):# largest positive integer that divides each of the integers
            gcd = i
             
    return gcd
    
    
'''
Computing private key for chosen p,q,e
'''
def KeyGeneration():
    p ,q, publicKey,privateKey= 0,0, 0,0 
    
    #2 large primes
    p = randprime(100,500)
    q =randprime (501,999)
 
    n=p*q #calc n
    EulerPhi = (p-1) *(q-1) #calc EulerPhi(n) = (p-1) (q-1)
    
    
    #find gcd (e, EulerPhi )= 1 
    while (computeGCD(publicKey,EulerPhi) != 1): 
        publicKey = random.randint(2,1000) #e
        

    #exhaustive search for private key (d), when d*e mod phi(n) =1. And d != e. 
    for i in range(1,EulerPhi):  
        if (publicKey*i ) %EulerPhi ==1 and publicKey!=i:
            privateKey = i
            break
    
    print("p, q, n, EulerPhi, publicKey, privateKey\n",p,q,n,EulerPhi,publicKey,privateKey,"\n") #debug
   
    return  publicKey,privateKey,n
 

'''
Compute the cipher text using the plain text and the public key.
'''
def Encryption (message,publicKey,n):
   
    listA = []
    for i in message:
        xStr = i.encode('utf-8')
        y=xStr.hex()
        listA.append(y)
    
    cipherText = []
    for i in listA:
        c=((int(i,16))**publicKey)%n #cipherText = (int(message)**publicKey ) % n 
        cipherText.append(c)
    
    return cipherText



'''
Compute the plain text using the cipher text and the private key.
'''
def Decryption (message,privateKey,n):
    
    plainText = " "
    txt = message.split(",")
    
    for i in txt:
        d=( int(i)**privateKey)%n #plainText = (int(message)**privateKey ) % n
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
    
Main()
