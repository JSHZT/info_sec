from user import User

hzt = User('hzt')
lyx = User('lyx')
wkq = User('wkq')

messages = 'there is a dog'

hzt.sign(messages)
lyxcheck = lyx.check(messages, hzt, hzt.crypto)
if lyxcheck['result']:
    print('{}验证签名成功！'.format(lyx.name))
else:
    print('{}验证签名失败，原因是:{}'.format(lyx.name, lyxcheck['reason']))
wkqcheck = wkq.check(messages, lyx, hzt.crypto)
if wkqcheck['result']:
    print('{}验证签名成功！'.format(wkq.name))
else:
    print('{}验证签名失败，原因是:{}'.format(wkq.name, wkqcheck['reason']))