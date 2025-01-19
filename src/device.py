class SmartLight:
    """Class to simulate a Smart Light device."""
    def __init__(self):
        self.state = "off"  # Initial state is off
        self.brightness = 0  # Initial brightness is 0%

    def turn_on(self):
        """Turn the smart light on."""
        self.state = "on"

    def turn_off(self):
        """Turn the smart light off."""
        self.state = "off"

    def set_brightness(self, brightness):
        """Set the brightness of the smart light."""
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            raise ValueError("Brightness must be between 0 and 100.")