'''
Created on Oct. 22, 2022
updated nov 6.

@author: Phoebe Schulman
'''


'''
class eg1: -OK

#class eg: when p=2,q=7,e=5 -> n = 14, euler = 6, d =11

encypt x= 2 -> 4
decpt y = 4 -> 2


---------
class eg2: -OK
 when p=3,q=11,e=3 -> n = 33, euler = 20, d =7
 
encypt x=4 -> 31
decpt y = 31 -> 4

------------
class eg3: -TODO #"A top secret! "-> "4120746f702073656372657421" in gneralll...without rsa..
 when p=F7E75FDC469067FFDC4E847C51F452DF,q=E85CED54AF57E53E092113E62F436F4F,e=0D88C3
  -> n = ?, euler = ?, d =?
 
encypt x="A top secret! "-> "4120746f702073656372657421"
decpt y = 4120746f702073656372657421 -> A top secret!
'''


#===============================================
'''
is prime 
https://geekflare.com/prime-number-in-python/

gcd
https://www.geeksforgeeks.org/gcd-in-python/
'''


import codecs
import random

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


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

    while  (not is_prime(p) or not is_prime(q) or p == q ) :
        p = random.randint(2,1000)
        q = random.randint(2,1000)
        #print(is_prime(p), is_prime(q))
    
    #p = F7E75FDC469067FFDC4E847C51F452DF 
    #q = E85CED54AF57E53E092113E62F436F4F 
   
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
    cipherText = ""
     
    #convert string x to hex.? #eg x is "2" or x is "a"
    
    #print(bytes(x,'utf-8').hex()) ?
    #if message.isdigit(): #x is "2"
    
    
    # x = 2 -> y = 4 for  eg
    cipherText = (int(message)**publicKey ) % n #int() works for num input... but not letters...
    
    return cipherText



'''
Compute the plain text using the cipher text and the private key.
'''
def Decryption (message,privateKey,n):
    plainText = ""

    #y = 4 -> x = 2 for  eg
    plainText = (int(message)**privateKey ) % n
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
#convertPrac()

#might need square and mutl #prime #gcd
