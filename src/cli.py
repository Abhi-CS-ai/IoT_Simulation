import SmartLight, Thermostat, SecurityCamera

def display_menu():
    """Display the main menu options."""
    print("\nIoT Device Monitor")
    print("===================")
    print("1. Turn Smart Light On/Off")
    print("2. Adjust Smart Light Brightness")
    print("3. Turn Thermostat On/Off")
    print("4. Adjust Thermostat Temperature")
    print("5. Turn Security Camera On/Off")
    print("6. Start/Stop Security Camera Recording")
    print("7. View Device Status")
    print("0. Exit")

def main():
    """Main function to handle user interaction."""
    # Initialize devices
    smart_light = SmartLight()
    thermostat = Thermostat()
    security_camera = SecurityCamera()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            action = input("Turn Smart Light (on/off): ").lower()
            if action == "on":
                smart_light.turn_on()
            elif action == "off":
                smart_light.turn_off()
            else:
                print("Invalid input!")

        elif choice == "2":
            try:
                brightness = int(input("Enter brightness (0-100): "))
                smart_light.set_brightness(brightness)
            except ValueError:
                print("Invalid brightness value!")

        elif choice == "3":
            action = input("Turn Thermostat (on/off): ").lower()
            if action == "on":
                thermostat.turn_on()
            elif action == "off":
                thermostat.turn_off()
            else:
                print("Invalid input!")

        elif choice == "4":
            try:
                temperature = float(input("Enter temperature (15-30°C): "))
                thermostat.set_temperature(temperature)
            except ValueError:
                print("Invalid temperature value!")

        elif choice == "5":
            action = input("Turn Security Camera (on/off): ").lower()
            if action == "on":
                security_camera.turn_on()
            elif action == "off":
                security_camera.turn_off()
            else:
                print("Invalid input!")

        elif choice == "6":
            if security_camera.state == "on":
                action = input("Start or Stop Recording (start/stop): ").lower()
                if action == "start":
                    security_camera.start_recording()
                elif action == "stop":
                    security_camera.stop_recording()
                else:
                    print("Invalid input!")
            else:
                print("Cannot record. Security Camera is off!")

        elif choice == "7":
            print("\nDevice Status:")
            print(f"Smart Light - State: {smart_light.state}, Brightness: {smart_light.brightness}")
            print(f"Thermostat - State: {thermostat.state}, Temperature: {thermostat.temperature}°C")
            print(f"Security Camera - State: {security_camera.state}, Recording: {security_camera.recording}")

        elif choice == "0":
            print("Exiting IoT Device Monitor. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()
