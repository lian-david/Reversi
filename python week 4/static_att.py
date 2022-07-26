class MyClass:
    #class attributes are shared between the objects
    static_var = 0  #class/static attribute 

    def __init__(self):
        #variables defined in constructor are instance attributes
        self.inst_var = 5   #instance attribute

    @staticmethod
    def do_something():
        print("This is a static method, you can invoke it without creating an object")

print(MyClass.static_var)

#can update class attribute outside of class
MyClass.static_var += 1
print(MyClass.static_var)

obj1 = MyClass()
obj1.inst_var = 10
obj2 = MyClass()
obj2.inst_var = 20

print(obj1.static_var)  #static variables can also be accessed via the instance
print(obj2.static_var)

obj1.instance_var = 5   #attribute added dynamically to the object

MyClass.do_something()