FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius / FAHRENHEIT_TO_CELSIUS_FACTOR) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)



def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Fahrenheit, Celsius, and Kelvin."""
    if from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)
    else:
        raise ValueError("Invalid temperature unit")

def main():
    """Main function to demonstrate temperature conversion."""
    print("Temperature Conversion Tool")
    value = float(input("Enter the temperature to convert: "))
    from_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
    to_unit = input("To unit (F/C): ").strip().upper()
    
    try:
        converted_value = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {converted_value:.2f} {to_unit}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()