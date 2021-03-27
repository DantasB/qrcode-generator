import os
from dotenv import load_dotenv

load_dotenv()


def get_env_parameters() -> tuple:
    """ Returns the environment variables"
    Returns:
        Tuple: the qrcode folder and the csv document folder
    """
    qrcode_folder = os.getenv("DIR_NAME")
    document = os.getenv("CSV_FILENAME")

    return (qrcode_folder, document)
