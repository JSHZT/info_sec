# 基于Hash实现的token生成器的账户管理类
本程序简单实现了一个账户管理类（可继续开发扩充功能），可嵌入到登录、注册等事宜的模块上，本程序对用户设定的密码加上用户专属的salt使用MD5方法计算散列值得到用户专属的token
## 系统接口组成
* 注册：输入用户名，密码即可注册

注册过程会随机赋予用户盐，盐和密码共同生成口令以供验证使用
* 登录：输入用户名和密码即可登录

系统会根据用户名索引到专属的盐和口令，并计算输入的密码和盐组合生成的散列值，若验证确认无误，则成功登录
* 验证
* 口令生成：采用md5方法生成密码和盐组合的串的散列值

## 运行程序
    python usr_info_manage.py --load <True/False> --path_to_data <your data path>