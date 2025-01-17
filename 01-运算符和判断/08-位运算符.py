# 位运算符用于对二进制数进行按位操作。这些操作主要应用于底层开发、系统编程、图像处理等领域。
# 位运算操作符以二进制位为基础，直接对整数的二进制表示进行操作。

# 按位与 (&)
# 对两个二进制位同时为 1 的位，结果为 1，否则为 0。

a = 5  # 0101
b = 3  # 0011
print(a & b)  # 1 (0001)

# 按位或 (|)
# 只要两个二进制位中有一个为 1，结果就是 1。

a = 5  # 0101
b = 3  # 0011
print(a | b)  # 7 (0111)

# 按位异或 (^)

# 两个二进制位不相同时结果为 1，相同时结果为 0。

a = 5  # 0101
b = 3  # 0011
print(a ^ b)  # 6 (0110)

# 按位取反 (~)
# 取反运算符对每一位进行反转，即 0 变 1，1 变 0。
# Python 中，按位取反操作不仅会取反，还会根据符号位调整结果，所以 ~x 实际结果是 -x-1。
a = 5  # 0101
print(~a)  # -6 (取反得到 1010)

# 左移 (<<)
# 将数字的二进制位左移若干位，右侧补 0，相当于乘以 2 的若干次方
a = 5  # 0101
print(a << 1)  # 10 (1010)

# 右移 (>>)
# 将数字的二进制位右移若干位，左侧根据符号位填充 0 或 1，相当于除以 2 的若干次方
a = 5  # 0101
print(a >> 1)  # 2 (0010)


# 位运算的实际应用
#
# 权限管理：用位操作来管理权限，常见于操作系统或程序的权限控制，比如文件权限可以用多个二进制位表示不同的权限位。
# 加密和解密：按位异或 (^) 常用于简单的加密和解密操作。
# 位图和图像处理：在位图处理中，每一个像素通常用一个或多个位来表示，可以通过位运算进行高效的像素操作。

