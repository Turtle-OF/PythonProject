import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO, filename="info.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")


current_date = datetime.now().strftime("%Y-%m-%d")
logging.info(f"Поточна дата: {current_date}")
