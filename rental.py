class Customer:
    def __init__(self, customer_id, name, contact_info, address, license_number):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.address = address
        self.license_number = license_number

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.customer_id},{self.name},{self.contact_info},{self.address},{self.license_number}\n")

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Contact: {self.contact_info}, Address: {self.address}, License: {self.license_number}"


class Car:
    def __init__(self, car_id, make, model, year, color, rental_price, availability=True):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.rental_price = rental_price
        self.availability = availability

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(
                f"{self.car_id},{self.make},{self.model},{self.year},{self.color},{self.rental_price},{self.availability}\n")

    def __str__(self):
        return f"Car ID: {self.car_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Price: {self.rental_price}, Available: {self.availability}"


class Rental:
    def __init__(self, rental_id, customer, car, rental_start_date, rental_end_date):
        self.rental_id = rental_id
        self.customer = customer
        self.car = car
        self.rental_start_date = rental_start_date
        self.rental_end_date = rental_end_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        # 假设租赁费用按天计算
        days = (self.rental_end_date - self.rental_start_date).days
        return days * self.car.rental_price

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(
                f"{self.rental_id},{self.customer.customer_id},{self.car.car_id},{self.rental_start_date},{self.rental_end_date},{self.total_cost}\n")

    def __str__(self):
        return f"Rental ID: {self.rental_id}, Customer: {self.customer.name}, Car: {self.car.make} {self.car.model}, Start: {self.rental_start_date}, End: {self.rental_end_date}, Total Cost: {self.total_cost}"
