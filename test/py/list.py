#-*-coding:utf-8-*-
#-----------------------list的使用----------------------------------

# 1.一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示
user=['liangdianshui','twowater','两点水']
print('1.产品用户')
print(user)

# 2.如果需要统计有多少个用户，这时候 len() 函数可以获的 list 里元素的个数
len(user)
print('\n2.统计有多少个用户')
print(len(user))

# 3.此时，如果需要知道具体的用户呢？可以用过索引来访问 list 中每一个位置的元素，索引是0从开始的
print('\n3.查看具体的用户')
print(user[0]+','+user[1]+','+user[2])

# 4.突然来了一个新的用户，这时我们需要在原有的 list 末尾加一个用户
user.append('茵茵')
print('\n4.在末尾添加新用户')
print(user)

# 5.又新增了一个用户，可是这个用户是 VIP 级别的学生，需要放在第一位，可以通过 insert 方法插入到指定的位置
# 注意：插入数据的时候注意是否越界，索引不能超过 len(user)-1
user.insert(0,'VIP用户')
print('\n5.指定位置添加用户')
print(user)

# 6.突然发现之前弄错了，“茵茵”就是'VIP用户'，因此，需要删除“茵茵”；pop() 删除 list 末尾的元素
user.pop()
print('\n6.删除末尾用户')
print(user)

# 7.过了一段时间，用户“liangdianshui”不玩这个产品，删除了账号
# 因此需要要删除指定位置的元素，用pop(i)方法，其中i是索引位置
user.pop(1)
print('\n7.删除指定位置的list元素')
print(user)

# 8.用户“两点水”想修改自己的昵称了
user[2]='三点水'
print('\n8.把某个元素替换成别的元素')
print(user)

# 9.单单保存用户昵称好像不够好，最好把账号也放进去
# 这里账号是整数类型，跟昵称的字符串类型不同，不过 list 里面的元素的数据类型是可以不同的
# 而且 list 元素也可以是另一个 list
newUser=[['VIP用户',11111],['twowater',22222],['三点水',33333]]
print('\n9.不同元素类型的list数据')
print(newUser)
