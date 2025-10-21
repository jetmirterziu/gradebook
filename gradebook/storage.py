"""gradebook/storage.py
Handles reading and writing data to JSON file.
Includes logging for load/save operations.
"""


import json
import os
import logging


# Configure logging
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to the JSON data file
DATA_FILE = os.path.join(os.path.dirname(
    __file__), "..", "data", "gradebook.json")


def load_data():
    if not os.path.exists(DATA_FILE):
        logging.warning(
            "Data file not found. Starting with an empty gradebook.")
        return {"students": [], "courses": [], "enrollments": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info("Loaded gradebook data successfully.")
            return data
    except json.JSONDecodeError:
        logging.error("JSON decode error: invalid file format.")
        return {"students": [], "courses": [], "enrollments": []}
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return {"students": [], "courses": [], "enrollments": []}


def save_data(data):
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info("Saved gradebook data successfully.")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
