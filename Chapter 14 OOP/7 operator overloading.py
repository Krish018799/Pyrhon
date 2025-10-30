# Operator overloading

# Each operator in Python is associated with a special method (also called a magic method or dunder method — double underscore).

# | Operator             | Method                      |
# | -------------------- | --------------------------- |
# | `+`                  | `__add__(self, other)`      |
# | `-`                  | `__sub__(self, other)`      |
# | `*`                  | `__mul__(self, other)`      |
# | `/`                  | `__truediv__(self, other)`  |
# | `//`                 | `__floordiv__(self, other)` |
# | `%`                  | `__mod__(self, other)`      |
# | `**`                 | `__pow__(self, other)`      |
# | `==`                 | `__eq__(self, other)`       |
# | `!=`                 | `__ne__(self, other)`       |
# | `>`                  | `__gt__(self, other)`       |
# | `<`                  | `__lt__(self, other)`       |
# | `>=`                 | `__ge__(self, other)`       |
# | `<=`                 | `__le__(self, other)`       |
# | `str()` or `print()` | `__str__(self)`             |


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)