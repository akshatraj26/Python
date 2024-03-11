# Exception class defined separately
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Class where exception is thrown
class Example:
    def some_method(self):
        # Some logic that might raise CustomException
        raise CustomException("An error occurred!")

# Main code to demonstrate exception handling
if __name__ == "__main__":
    example = Example()
    try:
        example.some_method()
    except CustomException as e:
        del example
        print("Destruction of object")
        # print(type(example))
        print("Caught custom exception:", e.message)

    finally:
        print("I will be executed everytime.")


