def str_counter(s):
    for i in set(s):
        count = 0
        for k in s:
            if i == k:
                count +=1
        print(i, count)


str_counter('abhhba')


def str_counter1(s):
    counter = {}
    for i in s:
        if counter.get(i):
            counter[i] +=1
        else:
            counter[i] = 1
    for i, count in counter.items():
        print(i,count)

str_counter1('ллллллввввввввввввввв')

print("щшхеоршщепьхуе9ы")