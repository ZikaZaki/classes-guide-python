
class Person:
  def __init__(self, name: str, age: int, ssn: str):
    self.name = name
    self.age = age
    self.__ssn = ssn # Private attribute

# Public method
def display_info(self) -> None:
  print(f"Name: {self.name}")
  print(f"Age: {self.age}")
  print(f"SSN: {self.ssn}")

@property
def ssn(self) -> str:
  masked_ssn = "XXX-XX-" + self.__ssn[-4:]
  return masked_ssn

def main() -> None:
  # Creating an instance of the Perosn class
  person1 = Person("Zack Ali", 30, "123-45-6789")

  # Accessing public method
  person1.display_info()

  # Output:
  # Name: Zack Ali
  # Age: 30
  # SSN: xxx-xx-6789

  # Accessing private attribute or method directly will raise an AttributeError
  # print(person1.__ssn) # This will raise an AttributeError
  # print(person1._Person__ssn) # This will work so it's not truly private, we still can access it via the "mangled attribute"