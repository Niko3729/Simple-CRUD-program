data = []
x = 0

def delete(d,x):
      if not d:
            print("Data is empty")
            print("\n")
            return
            
      for i in range(len(d)):
            print(i +1, "Name : ", data[x]["Name"], "   ", "Age : ", data[x]["Age"])
            x += 1
            a = int(input("Choose the data you want to delete by input the number : "))
            if a > len(d):
                  print("Data invalid")
                  return
            d.pop(a -1)
            if not d:
                  print("Data now is empty")
                  break

def modify(d, x):
        if not d:
              print("Data is empty")
              print("\n")
              return
        for i in range(len(d)):
            print(i +1,"Name : ", data[x]["Name"], "   ", "Age : ", data[x]["Age"])
            x += 1
        a = int(input("Choose data by you want to modify by input the number : "))
        if a > len(d):
                  print("Data Invalid")
        print("choose typedata you want to change by input the number")
        print("1). Name")
        print("2). Age")
        b = input("Change : ")
        index_ctrl = a-1
        if b == 2 or b == "2":
              change = int(input(" Input new age : "))
              d[index_ctrl]["Age"] = change
        if b == 1 or b == "1":
              change = input("Input new name : ")
              d[index_ctrl]["Name"] = change
            
        

def show(d, x):
    if not d:
          print("Data is empty")
          print("\n")
          return
    while True:
        for i in range(len(d)):
            print(i +1, "Name : ", data[x]["Name"], "   ", "Age : ", data[x]["Age"])
            x += 1
        done = input('Input D or d to get done : ')
        if done == "d" or done == "D":
            break

def inp(d):
    while True:
        name = str(input("Name : "))
        age = int(input("Age   : "))
        d.append({"Name" : name, "Age" : age})
        done = input("Input D or d to get done : ")
        if done == "D" or done == "d":
            print("\n")
            break

def hub(d, x):
    while True:
        print("==== The Hub ====")
        print("0). exit")
        print("1). Input ")
        print("2). Show ")
        print("3). Change")
        print("4). Delete")
        i = input("Choose menu with number : ")
        if i == 1 or i == "1":
            inp(d)
        if i == 0 or i == "0":
            break
        if i == 2 or i == "2":
            show(d, x)
        if i == 3 or i == "3":
              modify(d, x)
        if i == 4 or i == "4":
              delete(d, x)

hub(data, x)
