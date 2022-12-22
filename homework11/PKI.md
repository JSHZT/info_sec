# PKI操作报告
## 建立CA 创建自签名证书
* 安装openssl

* 确保openssl可以使用后，列出可用ECC曲线`openssl ecparam -list_curves`,如下图：
    ![](img\30.png)

* 在这里我使用prime256v1生成ECC秘钥对，使用ECC key生成CA证书,首先生成CA ECC私钥

    `openssl ecparam -out private/ec-cakey.pem -name prime256v1 -genkey`



    
* 然后生成CA证书

    `openssl req -new -x509 -days 3650 -config openssl.cnf -extensions v3_ca -key private/ec-cakey.pem -out cert/ec-cacert.pem`

    ![](img\31.png)
* 接下来，验证CA证书的内容和使用的签名算法

    `openssl x509 -noout -text -in cert/ec-cacert.pem`

    ![](img\32.png)
如上图可以看到，使用的是ESDSA签名算法去生成CA证书，而不是RSA
* 使用私钥验证CA证书

    `openssl x509 -noout -pubkey -in cert/ec-cacert.pem`
    ![](img\33.png)

* 从私钥导出公钥
    
    `openssl pkey -pubout -in private/ec-cakey.pem`
    ![](img\34.png)
    
    可以看到生成的公钥是相同的


## 使用CA私钥和证书签发服务端证书

* 进入server_certs目录，再一次使用曲线prime256v1生成ECC的私钥

    `openssl ecparam -out server.key -name prime256v1 -genkey`

* 生成CSR请求

    `openssl req -new -key server.key -out server.csr -sha256`
    ![](img\35.png)

* 使用ECC CA私钥，CA证书，对server.csr进行签名，生成服务端证书

    `openssl ca -keyfile ../private/ec-cakey.pem -cert ../cert/ec-cacert.pem -in server.csr -out server.crt -config ../openssl.cnf`
    ![](img\36.png)

* 验证证书是否有效时使用CA证书

    `openssl verify -CAfile ../cert/ec-cacert.pem server.crt`
    ![](img\37.png)

* 验证index.txt

    ![](img\38.png)
