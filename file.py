#Khai báo biến 
x= 10
name = "Võ Minh Tâm"
is_value = True
#if là từ khóa không thể là tên biến
1 if = 5 
#Toán tử số học 
#cộng
a= 5 
b= 3
result = a + b #ket quả là 8
#trừ
a=8
b= 4
result = a - b #ket quả là 4
#nhân
a= 6
b= 7
result = a * b #ket qua : 42
#chia
a= 20
b= 5
result = a / b #ket qua : 4 (kqua luon la 1 so thap phan neu co phan du )
#chia lấy nguyên
a= 20
b= 3
result = a // b #ket qua :6
#chia lấy dư
a= 20
b= 7
result = a % b #ket qua :6 (phan du cua 20 chia cho 7)
#lũy thừa
a= 2
b= 3
result = a ** b #ket qua :8 (2^3=8)
##cac toan tu logic
#phep toan and
x= 5
y=3
result= (x>2) and (y<4 ) #ket qua : True
#phep toan OR
x=5
y=3
result= (x>2) or (y>4) #ket qua : True
#phep toan NOT
x=5
result = not (x==5) #ketqua: False
#phep toan so sanh bang 
x=5
result = (x==5) #ketqua : True
#phep toan so sanh khong bang
x=5
result = (x!=3) #ketqua : True
#phep toan so sanh lon hon 
x=5
result1 = (x>3) #ketqua : True
result2 = (x<3) #ketqua : False
#phep toan so sanh nho hon
x=5
result1 = (x<3) #ketqua : False
result2 = (x>3) #ketqua : True
##nhap xuat du lieu
name = input("nhap ten cua ban:Vo Minh Tam ")
print("Ten cua ban la: ", name)
age = 21
print("Tuoi cua ban la: ", age)
#ngoai ra
print ("python", "la ", "ngon","ngu","lap","trinh", sep="-")
#ketqua:
print ("Xin chao",end="")
print("Cac ban!") #ketqua: Xin chao cac ban
##Cac cau truc dieu khien
#cau lenh dieu kien
x=10 
if x >5:
    print("x lon hon 5")
elif x==5:
    print("x bang 5")
else:
    print("x nho hon 5")
##vong lap for
fruits = [" apple","banana","cherry"]
for fruits in fruits:
    print("fruit")
#vong lau while
count =0 
while count <5:
    print("count")
    count +=1
##cau lenh nhay
#break
#tim so chia het cho 5 trong khoang tu 1 den 100
for i in range (1, 101):
    if i % 5 ==0:
        print(" so chia het cho 5 deu tien la",i)
        break
#continue
#in so chan tu 1 den 10 va bo qua cac so le
for i in range(1,11):
    if i % 2 != 0:
        continue
    print("i")
#pass
#kiem tra dieu kien, neu dung thuc hien, neu sai thi khong lam gi
x=5 
if x>10:
    print("x lon hon 10")
else:
    pass
##chuoi
#khai bao chuoi trong python
#su dung dau ngoac don
string_single_quotes ='day la 1 chuoi su dung dau ngoac don'
#su dung chuoi dau ngoax kep
string_double_quotes= "day la 1 chuoi su dung dau ngoac kep"
#su dung dau ngoac ba
string_triple_quotes= '''day la 1 chuoi su dung dau ngoac ba'''
#truy cap ky tu trong chuoi
my_string ="hello, Word!"
print(my_string[0]) #ket qua : H
print(my_string[7]) #ket qua : W
#cac phep xu lys chuoi trong python
#cat chuoi
my_string = "hello, Word"
print(my_string[7:]) # lay ki tu tu 7 den het : kqua 'Word
print(my_string[:5]) # lay ki tu tu dau denky tu thu 5 : kqua 'Hello'
print(my_string[3:8]) # lay ki tu thu 3 den ki tu thu 7 den het : kqua 'lo, W'
#ghepchuoi
string1="Hello"
string2="Word"
concatenated_string= string1+ ""+ string2# kqua Hello Word
#dodaichuoi
my_string = "Hello, Word"
length = len(my_string) #kqua 13
#1 so ham dung de xu ly chuoi trong python
my_string= "    Hello, Word!   "
print(my_string.strip())#laoi bo khoang trang
my_string="Hello, Word"
print(my_string.split(","))# phan tach chuoi
my_string="Hello, Word!"
print(my_string.replace("Hello", "Hi"))# thay the chuoi ket qua
##Ham
#khai bao ham
def my_funtion(parameter1, parameter2):
    result= parameter1 + parameter2
    return result
#phan loai ham
result = my_funtion(10, 20)
print(result)
#VD
def caculate_sum(a,b):
    result= a+b
    return result
sum_result = caculate_sum(10,20)
print("tong hai so la",sum_result)
#vs khai bao va goi ham khong co gtri tra ve
def greet(name):
    print("Xin chao",name)
greet("Alice")
##kieu du lieu co cau truc
#mang
from array import array
#VD
from array import array
int_array= array('i',[1,2,3,4,5])
float_array= array('f'[3.14,2.5,6.7])
#truy cap hpuong thuc trong mang
print(int_array[0])
print(float_array[2])
#capnhatgiatriphantutrongmang
int_array[2]=10
#caccphuong thuc cua mang array
int_array.append(6)
float_array.remove(6.7)
##List
#khai bao 1 danh sach
my_list= [1,2,3,4,5]
names= ["Alice", "Nam", "Tam"]
mixed_list= [10,"hello",3.14, True]
#truy cap vao 1phan tu trong ds
print(my_list[0])
print(names[2])
#cap nhat gia tri 1 phan tu trong danh sach
my_list[1]=20
print(my_list)
#them1phantuvaodanhsach
names.append("Tam")
print(names)
#xao1phantukhoidanhsach
del my_list[2]
print(my_list)
#duyetquatungptutrongdanhsach
for element in names:
    print(element)
##keiu Tuple
#khaibaoTuple
my_tuple = (1,2,3,4,5)
names= ("Tam","Nam","Thuy")
mixed_tuple= (10,"hello",3.14)
#truyx cap vao ptu trong tuple
print(my_tuple[0])
print(names[2])
#Cacphoungthuctrongtuple
#count
my_tuple= ('1','2','3','1','4','1')
print(my_tuple.count(1))
#index
my_tuple= ('a','b','c','d','b')
print(my_tuple.index('b'))
#kieu Dictionary
my_dict = {}
person = name {"name":"Tam","age":25,"city":"HochinhMinh"}
#truycapvaogiatri dictionary
print(person["name"])
print(person["age"])
#themhoacnhapgitri trong dictionary
person["email"]= "tam@gmail.com"
person["age"]= 21
#xoa1ptutrong dictionary
del person["city"]
age = person.pop("age")
#cacpthucdanhchodictionary
print(person.keys())
print(person.values())
print(person.items())
##OOP trong python
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def get_infor(self):
        return f"{self.brand} {self.model}"
my_car = Car ("toyota","Mec")
print(my_car.get_infor())
#khoitao(contructor)
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2
#vdsau
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def get_infor(self):
        return f"{self.brand} {self.model}"
my_car = Car ("toyota","Mec")
print(my_car.get_infor())
#thuoctinh
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1= attribute1
        self.attribute2= attribute2
    class_attribute= "Class Attribute"
#truy cap thuoc tinh
object= ClassName(value1, value2)
print(object_name.attribute1)
print(object_name.class_attribute)
#dinhnghia1phuongthuctrongpython
class ClassName:
    def method_name(self, parameter1, parameter2):
        return something
#truycapdoituongpthuctrong python
object_name = ClassName
object_name.method_name(value1, value2)
##kethua
#kethuadon
class ParentClass:
    # Định nghĩa thuộc tính và phương thức của lớp cha
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Tên:", self.name)

class ChildClass(ParentClass):
    # Định nghĩa thuộc tính và phương thức mới hoặc mở rộng từ lớp cha
    def __init__(self, name, age):
        super().__init__(name)  # Gọi hàm khởi tạo của lớp cha
        self.age = age

    def show_info(self):
        print("Tên:", self.name)
        print("Tuổi:", self.age)

# Sử dụng
child = ChildClass("Tam", 21)
child.show_name()   # Gọi phương thức của lớp cha
child.show_info()   # Gọi phương thức của lớp con
##DaKeThua
# Đa kế thừa: Một lớp con kế thừa từ nhiều lớp cha

class ParentA:
    def method_a(self):
        print("Phương thức từ ParentA")

class ParentB:
    def method_b(self):
        print("Phương thức từ ParentB")

class Child(ParentA, ParentB):
    def method_child(self):
        print("Phương thức của lớp Child")

# Sử dụng
child = Child()
child.method_a()      # Gọi phương thức từ ParentA
child.method_b()      # Gọi phương thức từ ParentB
child.method_child()  # Gọi phương thức của lớp Child

##1.4.6 Đa hình (Polymorphism)
#Đa hình ở thời điểm biên dịch
class Calculation:
    def add (self, a, b):
        return a + b 
    def add(self, a, b, c):
        return a + b + c
#Overriding (Ghi đè)
class Animal:
    def make_sound (self) :
        return "Generic sound"
class Dog(Animal):
    def make_sound (self) :
        return"Woof!"
#Đa hình ở thời điểm chạy 
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Hàm sử dụng đa hình: nhận đối tượng animal và gọi phương thức make_sound phù hợp
def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Kết quả: Woof!
print(animal_sound(cat))  # Kết quả: Meow!

#VD 
from abc import ABC, abstractmethod

# Lớp trừu tượng
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Lớp con thực hiện (định nghĩa phương thức cụ thể)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Sử dụng các đối tượng trừu tượng
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Kết quả: Woof!
print(cat.make_sound())  # Kết quả: Meow!
