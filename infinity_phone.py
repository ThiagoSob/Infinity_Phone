#Celphone Startup and The New Password Entrace 

import time

print("-----"*10)
print("\n\n")
time.sleep(1)
print("                  INFINITY PHONE")
print("\n\n")
time.sleep(1)
print("-----"*10)
print("\n\n")
time.sleep(1)
print("                     STARTUP")
print("\n")
time.sleep(1)
print("                       .")
time.sleep(1)
print("                       ..")
time.sleep(1)
print("                       ...")
print("\n\n")
time.sleep(1)
print("-----"*10)
print("\n\n")
time.sleep(1)
print("               PASSWORD REGISTRATION")
print("\n")
time.sleep(1)
senha_1 = 0
senha_2 = 1
tentativa = 3

while(senha_1 != senha_2):
    senha_1 = input(              "ENTER THE NEW PASSWORD: ")


    while(senha_1 != senha_2):
        time.sleep(1)
        senha_2 = input("ENTER THE NEW PASSWORD AGAIN: ")
        tentativa -= 1
        if (senha_1 == senha_2):
            time.sleep(2)
            break
        elif(tentativa != 0):
            print("THE SECOND ENTRECE WAS DIFERENT OF THE FIRST!")
            time.sleep(1)
            print("\n")
            print(f"YOU HAVE MORE {tentativa} TIMES!")
        elif (tentativa == 0):
            print("YOU FINISH YOUR CHANCES!\nTRY AGAIN SINCE FIRST ENTRACE!")
            break
    
    time.sleep(1)
    print("\n\n")
    time.sleep(1)
    print("-----"*10)
    time.sleep(1)
    print("\n\n")
    time.sleep(1)


print("     CRIATION OF THE NEW PASSWORD WAS SUCCESS!")
time.sleep(1)
print("\n\n")
time.sleep(1)
print("-----"*10)

time.sleep(1)
print("\n\n")
time.sleep(1)
print("                  INFINITY PHONE")
time.sleep(1)
print("\n\n")

print("-----"*10)
time.sleep(1)
senha = 0
tentativa_2 = 3
print("\n\n")
time.sleep(1)
for i in range(1, 4):
    tentativa_2 -= 1
    senha = input("PASSWOR: ")
    if(senha != senha_1):
        time.sleep(1)
        print("               ACCESS DENY!")
        time.sleep(1)
        print(f"         YOU HAVE MORE {tentativa_2} TIMES!")
        time.sleep(1)
        continue
    else:
        time.sleep(1)
        break
    
if(senha == senha_1):
    print("-----"*10)
    print("\n\n")
    time.sleep(1)
    print("                    STARTUP")
    print("\n\n")
    time.sleep(1)
    print("-----"*10)
else:
    print("-----"*10)
    print("\n\n")
    time.sleep(1)
    print("                 WRONG ENTRACE 3 TIMES!")
    time.sleep(1)
    print("\n")
    print("              YOUR INFINITY PHONE WAS BLOCK!")
    print("\n\n")
    time.sleep(1)
    print("-----"*10)