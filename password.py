#Cipher key
import time
import random
import os

def GetTheAccessKey_2() :
         InitialChar = '!+'
         for i in range (25):
                  RandomChar=chr(random.randint(65,115))
                  InitialChar+=RandomChar
         fname = "D:\\Project\\恒存项目\\Self exercise\\Py progra\\KeyFile\\Access Key.txt"
         fo = open(fname,"w+")
         fo.writelines("Access Key :"+InitialChar)
         fo.close()
         return InitialChar

def GetTheCipherKey_2() :
         FinalCipherKey = 0
         CipherKey = 0
         InitialCipherKey_0 = eval(str(time.perf_counter())[2::])
         InitialCipherKey_1 = eval(str(time.perf_counter())[2::])
         InitialCipherKey_2 = eval(str(time.perf_counter())[2::])
         InitialCipherKey_3 = eval(str(time.perf_counter())[2::])
         InitialCipherKey = [InitialCipherKey_0,InitialCipherKey_1,InitialCipherKey_2,InitialCipherKey_3]
         random.shuffle(InitialCipherKey)
         for Rounds_1 in range(3) :
                  RandomNumber =random.randint(1,500)
                  CipherKey = CipherKey+(InitialCipherKey[Rounds_1])*RandomNumber
                  FinalCipherKey +=CipherKey
         FinalCipherKey = str(FinalCipherKey)
         fname = "D:\\Project\\恒存项目\\Self exercise\\Py progra\\KeyFile\\Cipher Key.txt"
         fo = open(fname,"w+")
         fo.writelines("Cipher Key :"+FinalCipherKey)
         fo.close()
         return FinalCipherKey

def CheckingProgress() :
         Passwords = GetTheCipherKey_2()
         AccessKey = GetTheAccessKey_2()
         
         InputPasswords = input("Input the Cipher Key :")
         InputAccessKey = input("Input the Access Key :")
         if(InputPasswords==Passwords) :
                  if(InputAccessKey==AccessKey) :
                           return 1
                  else :
                           return 0
         else :
                  return 0
         
def secret() :
         print("OHHH,YOU GET MY SECRET!!CONGRATULATIONS!")
         
times=3
path = r'D:\Project\恒存项目\Self exercise\Py progra' 
if(str(os.path.exists("KeyFile"))=='False'):
         os.mkdir(path + './KeyFile')
while(times) :
         number = CheckingProgress()
         if(number == 1) :
                  secret()
                  times = 0
         else :
                  print("Wrong!!")
                  times-=1
                  print("YOU HAVE {:d} TIMES".format(times))
                  if(times==0) :
                           print("!!!ERROR!!!")
exit

