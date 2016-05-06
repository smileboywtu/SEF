# SEF
a symmetry data encryption based on fountain code

# 算法设计

假设密钥为: PRIMARY_KEY = b7b6...b0

密钥掩码为: MASK = 101

加密块为: B7B6B5...B0(共64位)

# 加密过程

**1.** 通过掩码和密钥获得初始key值:

``` c

// 获得初始
key = b2b1b0 ^ MASK

```

**2.** 通过key值获得初始加密块

``` c

x0 = B[key++ % 8]
x1 = x0 ^ B[key++ % 8]
x2 = x1 ^ B[key++ % 8]
x3 = x2 ^ B[key++ % 8]
...
// 直到
x7 = x6 ^ B[key % 8]

```

**3.** 得到新的数据模块:

将得到的x7, x6, x5, x4, ..., x0得到新的B7B6B5...B0

**4.** 获得新的key

``` c

// 循环获得key
key = b3b2b1 ^ MASK

```

**5.** 通过key值获得初始加密块

``` c

x0 = B[key++ % 8]
x1 = x0 ^ B[key++ % 8]
x2 = x1 ^ B[key++ % 8]
x3 = x2 ^ B[key++ % 8]
...
x7 = x6 ^ B[key % 8]

```

**6.** 得到新的数据块

通过x7x6x5...x0获得新的B7B6B5...B0


**7.** 重复以上步骤, 直到循环遍历所有的key

...

# 解密过程


**1.** 获得key7

``` c

key7 = b1b0b7 ^ MASK

```

**2.** 从第七轮加密数据中获得第六轮的数据

``` c

// 假设 最终的加密数据为 B7B6...B0

x7x6...x0 = B7B6...B0

B[key7] = x0
B[key7++ % 8] = x1 ^ x0
B[key7++ % 8] = x2 ^ x1
...
B[key7 % 8] = x7 ^ x6

```

# author
smileboywtu@gmail.com
