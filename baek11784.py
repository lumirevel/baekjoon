while True:
    try:
        txt = input()
        result = ""
        for i in range(0,len(txt),2):
            result += chr(int(txt[i:i+2], base = 16))
        print(result)
    except:
        break
