import logging


logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    result = 10 / 0
except Exception as e:
    logging.error(f"Помилка: {e}")

