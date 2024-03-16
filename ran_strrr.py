import random
import matrix_value_add as m
import con_hex as con
import vec_add as vc
def val(leng):
    i = random.randint(0, len(leng) - 1)
    return i

def Ch(IDS, co): 
    res = False
    if len(co) > 0:
        for kl in co:
            if kl == IDS:
                res = True
    return res

def add(stri, co):
    ran_val = val(stri)
    check = Ch(ran_val, co)
    if not check:
        return ran_val
    else:
        return add(stri, co)

def strr(stri):
    co = []
    ran_str = ""
    for i in stri:
        a = add(stri, co)
        ran_str += stri[a]
        co.append(a)
        hex_str=con.bin(ran_str)
        mtx=m.my_function(hex_str)
    ar=vc.reshape_list(co,mtx)
    return(mtx,ar)
def reverse(lis,sec):
    con_lis=""
    con_lis2=[]
    for i in lis:
        for j in i:
            cond=con.strin(str(j))
            if cond!='\x00':
                con_lis+=cond
            else:
                continue
    for i in sec:
        for j in i:
            if j==0 & 0 not in con_lis2 or j!=0:
                con_lis2.append(j)
            else:
                continue
    orig_str=reverse_process(con_lis,con_lis2)
    return orig_str
def reverse_process(output_str, order_list):
    # Combine the output string and order list into a list of tuples
    combined_data = list(zip(output_str, order_list))
    
    # Sort the list of tuples based on the order_list
    sorted_data = sorted(combined_data, key=lambda x: x[1])
    
    # Extract the characters from the sorted list to reconstruct the original input
    original_input = ''.join([char for char, _ in sorted_data])
    
    return original_input

