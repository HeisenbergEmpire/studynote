# 以下為本課借用上堂課的例子
class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print("Hello," + self.name)

# 以下為本課例子，子類Student繼承自Person，繼承的關係是person包含了student，student是person的一部份
# 可以用英文表達繼承就是，student is a person但不是所有person都是student
class Student(Person):
# 在子類Student中，若要使用父類Person的屬性，則必須使用super(),如下便使用了父類的name屬性
    def __init__(self,name,school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to' + self.school)
    def say_hello(self):
        super().say_hello()
        print('I am rather tired')
# 同時，一切的類皆為object（python語言）的子類，所以一切如str、int、float、list、都可以在class中以寫死方式使用
    def __str__(self):
        return f'Student {self.name} from {self.school}'


student = Student('Heisenberg', 'UMD') # 此處可以看見，特殊參數self為此class的主要物件，heisenberg為name，UMD為school
student.say_hello() # 對應def say_hello()那段
student.sing_school_song() # 對應def sing_school_song()那段
print(student) # 在class中寫死方式使用__str__()方法，就可以讓print()方法輸出的字串變成我們想要的

print()

# isinstance()方法，可以檢查一個物件是否屬於某個類別，如果是，則回傳True，否則回傳False
# 如果要檢查物件student是否為Student類別，則可以用isinstance(student,Student)
# 如果要檢查物件student是否為Person類別，則可以用isinstance(student,Person)
# 如果要檢查class Student是否為class Person的子類，則可以用issubclass(Student,Person)
print(f'Is this a student? {isinstance(student,Student)}')
print(f'Is this a person? {isinstance(student,Person)}')
print(f'Is Student a Person? {issubclass(Student,Person)}')

print()
# 多給一個單獨使用繼承object的類別的__str__()方法，就可以讓print()方法輸出的字串變成我們想要的
class Presenter:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print("Hello," + self.name)
    def __str__(self):
        return self.name

presenter = Presenter('Heisenberg')
print(presenter)
