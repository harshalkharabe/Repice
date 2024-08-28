import logging
import os

class CustomLogger:
    def __init__(self, log_level='INFO', log_file_name='custom.log', log_path='logs'):
        self.log_level = logging.getLevelName(log_level)
        self.log_file_name = log_file_name
        self.log_path = log_path
        
        # Create logs directory if it doesn't exist
        os.makedirs(self.log_path, exist_ok=True)

        # Configure the logger
        self.logger = logging.getLogger(log_file_name)
        # self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        # Create a new file handler with the updated log file name
        file_handler = logging.FileHandler(os.path.join(self.log_path, self.log_file_name))
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(filename)s:%(lineno)d - %(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        # Add the new file handler to the logger
        self.logger.addHandler(file_handler)
                
    def get_logger(self):
        return self.logger

# Example usage:
# logger_instance = CustomLogger(log_level=logging.DEBUG, log_file_name='myapp.log', log_path='logs')
# logger = logger_instance.get_logger()
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
