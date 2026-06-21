class MyClass():
    """A Simple Class Code"""
    i = 12345
    def f(self):
        return "helo world"

x = MyClass()

print(x.__doc__)
print(x.i)
print(x.f())


    