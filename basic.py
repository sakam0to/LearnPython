# any
print("any:")
lst = [True, False, False]
print(f"any({lst}):{any(lst)}")
lst = [False, False, False]
print(f"any({lst}):{any(lst)}")

dic = {"k1": "v1", "k2": "v2"}
print(f"any({dic}):{any(dic)}")
dic = {0: "v1", 0: "v2"}
print(f"any({dic}):{any(dic)}")

ran = range(1, 100)
print(f"any({ran}):{any(ran)}")
lst = [0, 0, 0]
print(f"any({lst}):{any(lst)}")

# built-in math
print("built-in math:")
num = -2
abs_num = abs(num)
print(f"num: {num} abs:{abs_num}")

divmod_num = divmod(7, 3)
print(f"divmod: 7 / 3 = {divmod_num[0]} ... {divmod_num[1]}")

pow_num = pow(2,4)
print(f"pow: 2^4 = {pow_num}")

round_num1 = round(1.3)
round_num2 = round(1.6)
round_num3 = round(1.5)
round_num4 = round(2.5)
print(f"round(1.3)={round_num1}, round(1.6)={round_num2}, round(1.5)={round_num3}, round(2.5)={round_num4} ")

array = list(range(1, 101))
sum_num = sum(array)

min_num = min(array)

max_num = max(array)

print(f"array: 1,2,3,...,98,99,100\nThe sum:{sum_num} min:{min_num} max:{max_num}")

# eval
print("eval:")
print(eval("2 + 2"))

print(eval("pow(2,2)"))

x = 4
print(eval("2 * x"))

# format
print("format:")
name = input("What's your name?")
string = "The input is {input}".format(input = name)

print(string)

# input
print("input:")
name = input("What's your name?")
print(f"hello, {name}!")

# isinstance
print("isinstance:")
foo = 123

print(isinstance(foo, int))

print(isinstance(foo, str))

print(isinstance(foo, (int, str)))


lst = [123, 'abc', 456, 'def']
str_lst = []

for item in lst:
    if isinstance(item, str):
        str_lst.append(item)

print(str_lst)

# map
print("map:")
lst = [1, 2, 3, 4, 5, 6]


def square(num):
    return num * num


def double(num):
    return num + num


result1 = map(square, lst)
result2 = map(double, lst)
print(f"squared result:{list(result1)}")
print(f"doubled result:{list(result2)}")

# reversed
print("reversed")
tuple_foo = (1,2,"ab")

print(list(reversed(tuple_foo)))

list_foo = [1,2,3,4,5,6]

print(list(reversed(list_foo)))

str_foo = "abcdefg123456"

print(list(reversed(str_foo)))

range_foo = range(5,11)

print(list(reversed(range_foo)))


# split
print("split:")
str_foo = "1 2 3 4 5 6 7 8 9"

print(str.split(str_foo, " ", 3))

# join
print("join")
str_foo = "123456789"
print(" ".join(str_foo))

lst = ["a", "b", "c"]
print(" ".join(lst))

tup = ("a", "b", "c", "d")
print("*".join(tup))

dic = {"a": 1, "b": 2}
print("*".join(dic))

