# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

# Implement the InvalidTempError exception class here
class InvalidTempError(Exception):
    """Raised when the oven is set to an invalid temperature"""
    def __init__(self, temperature: int):
        self.message = f"Invalid temperature setting: {temperature}"
        super().__init__(self.message)

class DigitalOven:
    def __init__(self):
        self.temp = 0
        self.min_temp = 100
        self.max_temp = 500

    def set_temp(self, temp):
        if temp == 0 or (self.min_temp <= temp <= self.max_temp):
            self.temp = temp
        else:
            raise InvalidTempError(temp)

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(f"Error - {str(e)}")
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

# An "InvalidTempError" Exception should be raised if the temperature
# is set below 100 degrees or above 500 degrees
oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
test_oven(500)
