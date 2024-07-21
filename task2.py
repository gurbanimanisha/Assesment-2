class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Create an instance of the Person class
person1 = Person("Manisha", 30)

# Call the display_details method
person1.display_details()