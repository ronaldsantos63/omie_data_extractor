import logging
import os


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    string_format = "%(asctime)-15s - [%(levelname)-5s] - [%(module)s:%(lineno)d] - " \
                    "%(message)s"
    #
    logging.basicConfig(
        level=logging.ERROR,
        format=string_format,
        datefmt="%d-%m-%Y as %H:%M:%S",
        handlers=[
            logging.FileHandler('logs/log.txt'),
            logging.StreamHandler()
        ]
    )
