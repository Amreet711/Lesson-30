class MyClass:
    __privateVar=27
    def __privMeth(self):
        print("I am inside MyClass")
    def hello(self):
        print(MyClass.__privateVar)
foo = MyClass()
foo.hello()
foo.__privMeth()