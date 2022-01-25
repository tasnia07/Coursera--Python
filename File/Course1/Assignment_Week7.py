largest=None
smallest=None
while True:
    num=input("Enter a number: ")
    if num == "done" :
        break
    try :
        inum=int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or largest< inum :
          largest=inum

    if smallest is None or smallest>inum :
         smallest=inum


print("Maximum is",largest)
print("Minimum is",smallest)
