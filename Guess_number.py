import random
print('''\
===============
โปรแกรมทายตัวเลข
===============''')
r = random.randint(1,99)
while True :
    Input = int(input("ใส่ตัวเลขที่ต้องทาย : "))
    if Input > r :
        print(f"!  เลข {Input} มากเกินไป")
    elif Input < r :
        print(f"!  เลข {Input} น้อยเกินไป")
    elif Input == r :
        print()
        print(f"ถูกต้องครับ, เลขที่สุ่มไว้คือ {r}")
        break
    
