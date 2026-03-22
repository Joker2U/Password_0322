x = 3
while x > 0:  
    x = x -1
    password = input("請輸入密碼:")
    if password == '1234':
        print("密碼正確")
    else :
        print("密碼錯誤")
        if x > 0:
            print(f"密碼錯誤還有{x}次機會")
        

            
