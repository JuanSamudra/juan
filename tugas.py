from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        """Abstract method untuk menyalakan mesin kendaraan"""
        pass

    @abstractmethod
    def stop_engine(self):
        """Abstract method untuk mematikan mesin kendaraan"""
        pass

    @abstractmethod
    def drive(self):
        """Abstract method untuk mengemudikan kendaraan"""
        pass

# Implementasi untuk mobil
class Car(Vehicle):
    def start_engine(self):
        return "The car's engine is started."

    def stop_engine(self):
        return "The car's engine is turned off."

    def drive(self):
        return "The car is driving on the road."

# Implementasi untuk motor
class Motorcycle(Vehicle):
    def start_engine(self):
        return "The motorcycle's engine is started."

    def stop_engine(self):
        return "The motorcycle's engine is turned off."

    def drive(self):
        return "The motorcycle is zooming through traffic."

# Penggunaan
car = Car()
print(car.start_engine())  # Output: The car's engine is started.
print(car.drive())         # Output: The car is driving on the road.
print(car.stop_engine())   # Output: The car's engine is turned off.

motorcycle = Motorcycle()
print(motorcycle.start_engine())  # Output: The motorcycle's engine is started.
print(motorcycle.drive())         # Output: The motorcycle is zooming through traffic.
print(motorcycle.stop_engine())   # Output: The motorcycle's engine is turned off.
