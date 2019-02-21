import scipy as sp
import matplotlib.pyplot as plt



'''
precision 浮点数输出精度位数（默认值8位）
suppress 是否 禁止 使用 科学记数法（默认为False）打印小浮点值
'''
sp.set_printoptions(precision=4, suppress=True)

# 以 \t 为分隔符
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
# print(data[:10])
# print(type(data))
# print(data.shape)

# 小时信息
x = data[:, 0]

# 某个小时的 Web 访问数
y = data[:, 1]

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

# sp.isnan(y) 返回一个布尔型的数组，用来表示数组项中的内容是否 合法
# 统计缺失值的数量
# print(sp.sum(sp.isnan(y)))

# 使用 ~ 在 x 和 y 中值选择 y 值合法的项
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# print(x)
# print(y)
# print(x.shape)

# 以 x 和 y 作为数据，初始化一个散点图
plt.scatter(x, y)

plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")

# 设置 x 轴的 刻度 及 与之对应 的 坐标
plt.xticks([w*7*24 for w in range(10)],
           ['week %i'%w for w in range(10)])


# sp.polyfit() 前两个参数为 数组，第三个参数为 拟合多项式的程度
# 返回值为 多项式系数，最小二乘拟合的残差，......
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

print('Model parameters: {}'.format(fp1))
print('residuals is {}'.format(residuals))

# 第一个训练模型
f1 = sp.poly1d(fp1)
print(type(f1))
print(error(f1, x, y))

# 在指定的间隔内返回均匀间隔的数字 sp.linspace(start, stop, 1000)
fx = sp.linspace(0, x[-1], 1000)
print(fx)

# 画线形图 x y 线宽
plt.plot(fx, f1(fx), linewidth=4)

# 显示图例 参数 loc 设置图例显示的位置
plt.legend(['d=%i'%f1.order], loc='upper right')

# 自动缩放 tight（固定）
plt.autoscale(tight=True)

# 打开或关闭轴网格 grid（格）
plt.grid()

# 显示图像
plt.show()

f2p = sp.polyfit(x, y, 2)
f2 = sp.poly1d(f2p)
print(error(f2, x, y))

# ---------------------------------
# 拐点
inflection = int(3.5*7*24)

# 拐点之前的数据
xa = x[:inflection]
ya = y[:inflection]

# 拐点之后的数据
xb = x[inflection:]
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print('Error inflection=%f' % (fa_error + fb_error))

# 使用拐點之後的數據進行2階擬合
fb2 = sp.poly1d(sp.polyfit(xb, yb, 2))

from scipy.optimize import fsolve

# fsolve() 可以找到一个函数的根
'''
  给出一个起始估计值 800
  返回由“func（x）= 0”定义的（非线性）方程的根 func(x)=fb2-100000
'''
reached_max = fsolve(fb2 - 100000, 800)/(7*24)

print("100,000 hits/hour excepted at week {}".format(reached_max[0]))
