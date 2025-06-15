from src.Sample_ML_Project.logger import logging
from src.Sample_ML_Project.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The execution has started")
    
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero error occurred")
        raise CustomException(e, sys)