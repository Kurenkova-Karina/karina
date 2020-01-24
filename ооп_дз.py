1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    def __init__(self, color):
        print("Светофор готов к работе")
        self._color = str(color)

    def running:  не понимаю, что именно нужно сделать(




2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, length, width):
        self.__length = int(length)
        self.__width = int(width)

    def method(self, length, width):
        weight = int(input("Введите массу: "))
        thickness = int(input("Введите толщину: "))
        result = length * width * weight * thickness
        print (result)

road = Road(20, 5000)
road.method(20, 5000)

3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = input("Введите имя сотрудника: ")
    surname = input("Введите фамилию сотрудника: ")
    position = input("Введите позицию: ")
    __income = {'wage': 50000, 'bonus': 15000}

class Position (Worker):

     def get_full_name (self):
         print(self.name + self.surname)

    def get_total_income(self):
        print (self._Worker__income['wage'] + self._Worker__income['bonus'])

position = Position()
position.get_total_income()



4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = is_police

    def go(self):
        print("car is going")

    def stop(self):
        print ("car stops")

    def turn (self, direction):
        if direction == "right":
            print ("car goes right")
        elif direction == "left":
            print ("car goes left")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
            print ("Ваша скорость: %d .Скорость превышена" %(self.speed))
        else:
            print ("Ваша скорость: %d"  %(self.speed))


towncar = TownCar(65) #проверим
towncar.show_speed(65)

class SportCar(Car):
   pass

class PoliceCar (Car):
   pass


class WorkCar (Car):
   def show_speed(self, speed):
       if speed > 40:
           print ("Ваша скорость: %d .Скорость превышена" %(self.speed))
       else:
           print ("Ваша скорость: %d"  %(self.speed))

создадим экземпляры

sportcar = SportCar(80, "red", "car", False )
sportcar.go()

workcar = WorkCar(50, "rose", "folkswagen", False)
workcar.turn("right")

policecar = PoliceCar(40, "white", "Poliecar", True)
policecar.stop()





5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = str(title)

    def draw(self):
        print("Запуск отрисовки")

class Pen (Stationery):

    def draw(self):
        print("Ручка пишет")

class Pencil (Stationery):

    def draw(self):
        print("Карандаш рисует")

class Handle (Stationery):

    def draw(self):
        print("Маркер пишет")

проверка
handle = Handle("handle")
handle.draw()

pencil = Pencil("pencil")
pencil.draw()

pen = Pen ("pen")
pen.draw()


