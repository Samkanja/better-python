from dataclasses import dataclass
import string
import random
from typing import Dict,Any

@dataclass
class VehicleInfo:
    brand : str 
    catalogue_price: int
    electric: bool

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price
    def display(self):
        print(f'Brand: {self.brand}')
        print(f'Payable tax: {self.compute_tax()}')


@dataclass
class Vehicle:
    id: str
    licence_plate:str
    info:VehicleInfo

    def display(self):
        print(f'ID: {self.id}')
        print(f'License plate: {self.licence_plate}')
        self.info.display()

class VehicleRegistry:

    vehicle_info = {}
    def add_vehicle_info(self, brand,electric,catalogue_price) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand,catalogue_price,electric)

    def __init__(self) -> None:
        self.add_vehicle_info('Tesla Model 3',True,60000)
        self.add_vehicle_info('Volkswagen ID3',True,35000)
        self.add_vehicle_info('BMW 5',False,45000) 

    def generate_vehicle_id(self, length:int) -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self,id:str) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.digits,k=2))}-{''.join(random.choices(string.ascii_uppercase,k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        licence_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, licence_plate,self.vehicle_info[brand])

class Application:
    def register_vehicle(self, brand:str):
        registry = VehicleRegistry()

        return registry.create_vehicle(brand)

    
app = Application()
vehicle =app.register_vehicle('BMW 5')
vehicle.display()