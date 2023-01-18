"""
We want to add the capability to the software to reset the laptop to the factory settings.
This involves the following steps:

-Format the hard drive.
-Make sure the machine name is set to "DULL", which is the name of the company that produced the laptop.
-Install the os.
-Create an admin user with password "admin"

a) Extend the program with this capability relying on object-oriented programming.
b) Write another version of the same program, but this time, don't extend the class with new capabilities,
use a separate function instead. How would you describe the differences between the two versions?
"""
from dataclasses import dataclass, field
from functools import partial
from typing import Callable, Iterable, Union


@dataclass
class Laptop:
    machine_name: str = "DULL"

    def install_os(self) -> None:
        print("Installing OS")

    def format_hd(self) -> None:
        print("Formatting the hard drive")

    def create_admin_user(self, password: str) -> None:
        print(f"Creating admin user with password {password}.")

    def reset_to_factory(self, reset_password: str) -> None:
        self.format_hd()
        if self.machine_name != "DULL":
            print("Machine name not 'DULL' ")
        self.install_os()
        self.create_admin_user(password=reset_password)


my_laptop = Laptop()
print(my_laptop)
print(f"Resetting my laptop: ")
my_laptop.reset_to_factory("reset_pass")
