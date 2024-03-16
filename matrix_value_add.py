def my_function(s,k=1):
    result = []
    for i in range(0, len(s), k):
        sub = s[i:i+k]
        result.append(list(sub))

    if len(result[0]) < len(result):
        b=my_function(s, k + 1)
    else:
        a=add_zero(result)
        return a
    c=ch(b)
    return c
def ch(result):
    if len(result[0]) != len(result):
        a=add_row(result)
        return a
    else:
        return result
def add_zero(s):
    fs=len(s[0])
    fl=len(s[-1])
    ads=[]
    if fs>fl:
        ad=fs-fl
        for i in range(0,ad,1):
            ads.append(0)
        for i in ads:
            s[-1].append(i)
    return s
def add_row(s):
    fs=len(s[0])
    fl=len(s)
    ads=[]
    if fs>fl:
        ad=fs-fl
        for i in range(0,ad,1):
            ads.append(0)
        s.append(ads)
    ka=add_zero(s)
    return ka
