import string
def main():
    d = dict(zip(string.lowercase,string.lowercase[2:]+string.lowercase[:2]))
    result=""
    '''msg="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."'''
    msg=raw_input()
    for i in msg:
        try:
            result +=d[i]
        except:
            result +=i
    print result
    


if __name__=="__main__":
    main()
