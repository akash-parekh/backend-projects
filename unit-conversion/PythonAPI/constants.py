from enum import Enum
from pydantic import BaseModel


class convertUnitsRequest(BaseModel):
    type: str
    from_unit: str
    to_unit: str
    value: float

class HeightUnit(Enum):
    MILIMETER = 'mm'
    CENTIMETER = 'cm'
    METER = 'm'
    KILOMETER = 'km'
    INCH = 'in'
    FOOT = 'ft'
    YARD = 'yd'
    MILE = 'mi'

# Conversion rates to meter
HEIGHT_TO_METER = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1,
    'km': 1000,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344,
}
# Conversion rates from meter
HEIGHT_FROM_METER = {
    'mm': 1000,
    'cm': 100,
    'm': 1,
    'km': 0.001,
    'in': 39.3701,
    'ft': 3.28084,
    'yd': 1.09361,
    'mi': 0.000621371,
}

def convert_height(value, from_unit, to_unit):
    if from_unit not in HEIGHT_TO_METER or to_unit not in HEIGHT_FROM_METER:
        raise ValueError(f"Invalid height unit: {from_unit} or {to_unit}")
    value_in_meter = value * HEIGHT_TO_METER[from_unit]
    return value_in_meter * HEIGHT_FROM_METER[to_unit]

class WeightUnit(Enum):
    MILIGRAM = 'mg'
    GRAM = 'g'
    KILOGRAM = 'kg'
    TONNE = 't'
    OUNCE = 'oz'
    POUND = 'lb'
    STONE = 'st'

# Conversion rates to kilogram
WEIGHT_TO_KG = {
    'mg': 1e-6,
    'g': 1e-3,
    'kg': 1,
    't': 1000,
    'oz': 0.0283495,
    'lb': 0.453592,
    'st': 6.35029,
}
# Conversion rates from kilogram
WEIGHT_FROM_KG = {
    'mg': 1e6,
    'g': 1e3,
    'kg': 1,
    't': 0.001,
    'oz': 35.27396,
    'lb': 2.20462,
    'st': 0.157473,
}

def convert_weight(value, from_unit, to_unit):
    if from_unit not in WEIGHT_TO_KG or to_unit not in WEIGHT_FROM_KG:
        raise ValueError(f"Invalid weight unit: {from_unit} or {to_unit}")
    value_in_kg = value * WEIGHT_TO_KG[from_unit]
    return value_in_kg * WEIGHT_FROM_KG[to_unit]

class TemperatureUnit(Enum):
    CELSIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")