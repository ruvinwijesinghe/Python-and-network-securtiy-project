import hashlib

def Convert_Text_MD5(result):
    Convert_result=hashlib.md5(result.encode())
    print(Convert_result.hexdigest())

x= input("Enter your text")
Convert_Text_MD5(x)
    
    
