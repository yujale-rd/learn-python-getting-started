# 在 Python 中，变量的类型转换（也称为类型强制转换）是指将一种数据类型转换为另一种数据类型。
# Python 提供了多种内置的类型转换函数，可以在不同类型之间进行转换。常见的转换操作有整型、浮点型、字符串、布尔型等。

"""
常见的类型转换函数

- int()：将数据转换为整型
- float()：将数据转换为浮点型
- str()：将数据转换为字符串
- bool()：将数据转换为布尔型
"""

"""
2. 各种数据类型之间的转换规则

(1) 整型 (int)
	•	浮点型：截掉小数部分，不四舍五入。
	•	字符串：必须是数字字符串（如 "123"），否则抛出 ValueError。
	•	布尔型：True 转为 1，False 转为 0。

(2) 浮点型 (float)
	•	整型：直接转换为浮点形式（如 123 → 123.0）。
	•	字符串：必须是合法的浮点数字符串（如 "123.45"）。
	•	布尔型：True 转为 1.0，False 转为 0.0。

(3) 字符串 (str)
	•	整型/浮点型：直接转换为字符串形式。
	•	布尔型：True 转为 "True"，False 转为 "False"。

(4) 布尔型 (bool)
	•	以下值被视为 False：
	•	数字：0 或 0.0
	•	空字符串：""
	•	空集合、列表、字典等：[]、{}、()
	•	特殊值：None
	•	其他任何非零或非空值被视为 True。
"""

"""
3. 注意事项
	1.	int() 和 float() 转换时需确保输入合法
	•	"123abc" 或 "12.3.4" 等非法字符串无法转换为数值。
	•	转换前可使用 str.isdigit() 检查。
	
	
		2.	str() 函数不会报错：
	•	任何数据类型都可以转换为字符串，不会引发异常。
	3.	float() 转换小数点字符串：
	•	"12.34" 合法，可以转换。
	•	"12,34"（逗号分隔）非法，不支持直接转换。
	4.	bool() 的隐性转换：
	•	许多情况会隐式调用 bool()，如 if 条件判断等。
"""

# 测试数据
int_value = 10
float_value = 123.456
bool_value = True
str_int = "123"
str_float = "123.456"
str_invalid = "hello"

# int 转换
print(f"int -> float: {float(int_value)}")
print(f"int -> str: {str(int_value)}")
print(f"int -> bool: {bool(int_value)}")

# float 转换
print(f"float -> int: {int(float_value)}")  # 截断小数
print(f"float -> str: {str(float_value)}")
print(f"float -> bool: {bool(float_value)}")

# str 转换
print(f"str (int) -> int: {int(str_int)}")
print(f"str (float) -> float: {float(str_float)}")
try:
    print(f"str (invalid) -> int: {int(str_invalid)}")  # 抛出异常
except ValueError:
    print("无法将无效字符串转换为 int")

# bool 转换
print(f"bool -> int: {int(bool_value)}")
print(f"bool -> float: {float(bool_value)}")
print(f"bool -> str: {str(bool_value)}")