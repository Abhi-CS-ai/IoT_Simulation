# src/data_generation.py

import random

def generate_smart_light_data():
    """Generate random brightness for SmartLight."""
    return random.randint(0, 100)

def generate_thermostat_data():
    """Generate random temperature for Thermostat."""
    return round(random.uniform(18.0, 30.0), 1)

def generate_security_camera_data():
    """Generate random recording status for SecurityCamera."""
    return random.choice([True, False])
