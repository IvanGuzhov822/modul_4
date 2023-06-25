def check_palindrom(s):
    count = 0
    for i in range(len(s)//2):
        if s[i] == s[-1-i]:
            count += 1
            print(count)
    if count == len(s) // 2:
        return True
    else:
        return False
    
print(check_palindrom('rfvcec'))

