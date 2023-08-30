from dataclasses import dataclass
from functools import cached_property
from email_tools.service import EmailService

SMTP_SERVER = "smtp.gmail.com"
PORT = 465
EMAIL = "hi@zikazaki.com"
PASSWORD = "password"

def bmi(weight: float, height: float) -> float:
    return weight / (height**2)

def bmi_category(bmi_vlaue: float) -> str:
    if bmi_vlaue < 18.5:
        return "Underweight"
    elif bmi_vlaue < 25:
        return "Normal"
    elif bmi_vlaue < 30:
        return "Overweight"
    else:
        return "Obese"
        
@dataclass
class Stats:
    age: int
    gender: str
    height: float
    weight: float
    blood_type: str
    eye_color: str
    hair_color: str
    
@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    country: str
    postal_code: str
    
    def __str__(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.country}, {self.postal_code}"

@dataclass
class Person:
    name: str
    address: Address
    email: str
    phone_number: str
    stats: Stats
    
    def split_name(self) -> tuple[str, str]:
        first_name, last_name = self.name.split(" ")
        return first_name, last_name
    
    def update_email(self, email: str) -> None:
        self.email = email
        # send email to the new address
        email_service = EmailService(SMTP_SERVER, PORT, EMAIL, PASSWORD)
        email_service.send_message(
            self.email,
            "Your email has been updated.",
            "Your email has been updated. If this was not you, you have a problem."
        )

def main() -> None:
    # creatre a stats 
    stats = Stats(
        age = 30,
        gender = "male",
        height = 1.72,
        weight = 65.7,
        blood_type = "O+",
        eye_color = "black",
        hair_color = "black"
    )
    
    # create an address
    address = Address(
        address_line_1 = "123 Main St",
        address_line_2 = "Apt 1",
        city = "New York",
        country = "USA",
        postal_code = "12345"
    )
    
    # create a person
    person = Person(
        name = "ZikaZaki",
        address = address,
        email = "example@gmail.com",
        phone_number = "7777878787",
        stats = stats
    )
    
    # compute the BMI
    bmi_value = bmi(person.stats.weight, person.stats.height)
    print(f"Your BMI is {bmi_value:.2f}")
    print(f"Your BMI category is {bmi_category(bmi_value)}")
    
if __name__ == "__main__":
    main()
