x = 3
while x < 4:  
    password = input("請輸入密碼:")
    if password == '1234':
        print("密碼正確")
    else :
        print(f"密碼錯誤還有{x}次機會")
        x = x -1
        if x == 0:
            print("無法再嘗試程式結束")
            
