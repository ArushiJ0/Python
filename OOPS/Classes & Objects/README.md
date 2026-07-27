# Classes & Objects

Class is a blueprint for creating objects. Object is a real instance 

class class_name:
     def __init__(self, attribute):         //constructor 
     
     self.attribute = attribute      //instance_vaiable 
     
object_name = class_name()    //creating object

object_name.method()             // calling instance method

### Property -

It allows method to behave like an attribute and access method without parentheses.

@property - It is a getter and used to access a private attribute.

@property.setter - Used to change the value of a private attribute.

(@ is a decorator)

- @classmethod makes the first parameter ‘cls’ refer to the class instead of the instance ‘self’.
- @staticmethod makes a method static which does not require any self or object to be created. For that reason it does not require __init__
- @abstractmethod imported from abc; it is used to make class method compulsory for the child class to use

Method Overriding - when a child class inherits a parent class, the method in parent class with the same name in child class can be rewritten and Python reads the child class method and ignores the parent class method.


### Key Takeaways -

- self keyword is used to refer to the current object.
- Instance variable is used for objects whereas local variable is used in functions or methods.
- To make attributes private add __ before the attribute name.
- In method, when referring to a class data we ‘cls’ instead of self .
- Inheritance of class - class_name(parent_class_name);It uses super() keyword which inherits the attributes of the parent class. 
- __add__ is a special method which is automatically called if + operator is used.
- __enter__ & __exit__ are special method automatically called when ‘with’ statements are used.
- Method chaining is calling one method after another on same object with using self as return.
