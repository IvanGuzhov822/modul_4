a = [1,2,3]
for i in range(1,len(a)):
    print(i)

for k in range( min(len(strs[i]), len(strs[i-1]))):
               if strs[i][k] != out[k]:
                   out = out[:k]

        strs = sorted(strs)
        out = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                out += strs[0][i]
            else:
                return out
        return out

if ((one in s) and (two not in s)) or ((s.find(one) > s.find(two)) or (s.find(two)-s.find(one)!=1)):
            return False
        if ((three in s) and (four not in s)) or (s.find(three) > s.find(four) or (s.find(four)-s.find(three)!=1)):
            return False
        if ((five in s) and (six not in s)) or (s.find(five) > s.find(six) or (s.find(six)-s.find(five)!=1)):
            return False
        return True

if len(s) == 1:
            return False
        if (one in s and two in s) or (three in s and four in s) or (five in s and six in s):
            if (s.find(two) > s.find(one)) and (s.find(two)-s.find(one)==1):
                return True
            elif (s.find(four) > s.find(three)) and (s.find(four)-s.find(three)==1):
                return True
            elif (s.find(six) > s.find(five)) and (s.find(six)-s.find(five)==1):
                return True
        else:
            return False