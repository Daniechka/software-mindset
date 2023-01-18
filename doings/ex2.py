"""
create a system for managing customers' phone plans.
write a few dataclasses representing the data structure of their application.
they have
customers (name, address, email address),
phones (brand, model, price, serial number)
plans (
    which refer to a customer,
    a phone,
    a start date,
    the total number of months in the contract,
    a monthly price,
    whether the phone is included in the contract
    )
"""
from dataclasses import dataclass, field
from datetime import datetime


def calculate_months() -> int:
    return 1


@dataclass
class Customer:
    """name, address, email address"""

    name: str
    # address : str
    city: str
    street: str
    postcode: str
    email_address: str


@dataclass
class Phone:
    """brand, model, price, serial number"""

    brand: str
    model: str
    price: int
    serial_number: str
    pass


@dataclass
class Plan:
    """
    refers to a customer,
    a phone,
    a start date,
    the total number of months in the contract,
    a monthly price,
    whether the phone is included in the contract
    """

    customer: Customer
    phone: Phone
    startdate: datetime
    price_per_month: int
    contract_months: int = field(init=False, default_factory=calculate_months)
    phone_included: bool = field(init=False, default=True)


my_customer = Customer(
    name="Mark",
    city="Oslo",
    street="Drammenveien",
    postcode="AB1234",
    email_address="jk@post.wrld",
)

phone = Phone(brand="Cellphone", model="Best", price=100, serial_number="ab123")

johns_plan = Plan(
    customer=my_customer, phone=phone, startdate=datetime.today(), price_per_month=10
)

print(my_customer)
print(phone)
print(johns_plan)
