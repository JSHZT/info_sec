import rsa
import hashlib

CA = {}

class User:
    def __init__(self,name):
        self.name = name
        self.crypto = ''
        (self.pubkey,self.privkey) = rsa.newkeys(512)
        self.applyKey(self.name,self.pubkey)
    
    def sign(self, str):
        self.crypto = self.rsaEncrypt(hashlib.md5((str + self.name).encode()).hexdigest(),self.privkey)
        return self.crypto

    def check(self, str, user, crypto):
        if user.name not in CA:
            return {
                'result': False,
                'reason': "此用户没有申请数字证书\n"
            }
        else:
            pubk = CA[user.name]
            if self.rsaDecrypt(hashlib.md5((str+user.name).encode()).hexdigest(),crypto,pubk):
                return {
                'result': True
                }
            else:
                return {
                'result': False,
                'reason': "密文内容被更改，或签名用户不正确\n"
                }
                
    def rsaEncrypt(self, str, privk):
        content = str.encode('utf-8')
        crypto = rsa.sign(content, privk, 'MD5')
        return crypto
    
    def rsaDecrypt(self, mess, signa, pubk):
        try:
            rsa.verify(mess.encode(),signa,pubk)
        except rsa.VerificationError:
            result = False
        else:
            result = True
        return result
    
    def applyKey(self, name, pubk):
        CA[name] = pubk