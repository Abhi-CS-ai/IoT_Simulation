# src/logging.py

import logging

# Configure the logging format and file
logging.basicConfig(
    filename="device_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def log_device_data(device_name, data):
    """Log data for a specific device."""
    logging.info(f"{device_name}: {data}")
