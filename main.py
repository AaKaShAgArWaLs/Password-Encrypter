import ran_strrr as ra
import mat_op as mo
def encrypt(pas):

    enc_pass,sec_c=ra.strr(pas)


    enc_pass,sec_c=mo.mat_sub(enc_pass,sec_c)

    enc_pass,sec_c=mo.mat_multiply(enc_pass,sec_c)

    enc_pass,sec_c=mo.transpose(enc_pass,sec_c)

    sec_c,enc_pass=mo.transpose(sec_c,enc_pass)
    return sec_c,enc_pass
def decrypt(enc_pass,sec_c):

    enc_pass,sec_c=mo.transpose(enc_pass,sec_c)
    sec_c,enc_pass=mo.transpose(sec_c,enc_pass)
    enc_pass,sec_c=mo.mat_divide(enc_pass,sec_c)
    enc_pass,sec_c=mo.mat_add(enc_pass,sec_c)
    dcyp_pass=ra.reverse(enc_pass,sec_c)
    return dcyp_pass
pas=input("Enter Pass to Encrypt: ")
sec_c,enc_pass=encrypt(pas)
print("Your Encrypted Matrix=",enc_pass,"\nYour Secret Key is:",sec_c)
inp=int(input("Enter 1 to Decrypt:"))
if inp==1:
    dcyp_pass=decrypt(enc_pass,sec_c)
    print("Decrypted Pass= ",dcyp_pass)
    inp=int(input("Press 1 to close: "))
    if inp==1:
        exit(1)