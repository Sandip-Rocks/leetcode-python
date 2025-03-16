import logging

# Configure logging to display DEBUG level messages
logging.basicConfig(level=logging.DEBUG)

def div(x, y):
    logging.debug(f"div execution started with x={x}, y={y}")
    return x / y

# User Input
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

try:
    result = div(x, y)
    print("Result:", result)
except ZeroDivisionError:
    logging.error("Cannot divide by zero!")
except Exception as e:
    logging.error(f"Something went wrong: {e}")
