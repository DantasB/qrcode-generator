import asyncio
import aiohttp
import os


def build_qrcode_url(url: str) -> str:
    """ Returns the formated url to download the qr_code.
    Args:
        url (str): the link that's in the qrcode
    Returns:
        str: the qrcode bytes
    """
    return f"https://qr-generator.qrcode.studio/qr/custom?download=true&file=png&data={url}&size=1000&config=%7B%22body%22%3A%22circular%22%2C%22eye%22%3A%22frame12%22%2C%22eyeBall%22%3A%22ball14%22%2C%22erf1%22%3A%5B%5D%2C%22erf2%22%3A%5B%5D%2C%22erf3%22%3A%5B%5D%2C%22brf1%22%3A%5B%5D%2C%22brf2%22%3A%5B%5D%2C%22brf3%22%3A%5B%5D%2C%22bodyColor%22%3A%22%23000000%22%2C%22bgColor%22%3A%22%23FFFFFF%22%2C%22eye1Color%22%3A%22%23000000%22%2C%22eye2Color%22%3A%22%23000000%22%2C%22eye3Color%22%3A%22%23000000%22%2C%22eyeBall1Color%22%3A%22%23000000%22%2C%22eyeBall2Color%22%3A%22%23000000%22%2C%22eyeBall3Color%22%3A%22%23000000%22%2C%22gradientColor1%22%3A%22%22%2C%22gradientColor2%22%3A%22%22%2C%22gradientType%22%3A%22linear%22%2C%22gradientOnEyes%22%3A%22true%22%2C%22logo%22%3A%22%22%2C%22logoMode%22%3A%22default%22%7D"


async def download_qrcode(content_url: str) -> bytes:
    """ Access the QRCode-monkey page and generates the qrcode.
    Args:
        content_url (str): the link that's in the qrcode
    Returns:
        bytes: the qrcode bytes
    """
    async with aiohttp.ClientSession() as session:
        qr_code = await session.get(build_qrcode_url(content_url))
        qr_code_content = await qr_code.read()

        return qr_code_content


def save_qrcode(path: str, content) -> None:
    """Writes the document bytes in the path
    Args:
        content (bytes): bytes of the qrcode image 
        path (str): path to save the qrcode image 
    """
    with open(path, "wb") as f:
        f.write(content)


def is_not_valid_url(url: str) -> bool:
    """Returns True if there's no http in the url

    Args:
        url (str): the url to be used in the qrcode

    Returns:
        bool: True if there's no url
    """
    if('http' not in url):
        print(f"[Warn] Couldn't generate qrcode for page {url}")
        return True
    return False


def create_subdir(path: str) -> str:
    """ Creates the folder directory
    Args:
        path (str): the folder to be created
    Returns:
        str: the path string
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    return path


def treat_category(category: str) -> str:
    """ Treats a list of string
    Args:
        category (str): the category of an url

    Returns:
        str: the category treated
    """
    return category.lower().strip()


def get_qrcode_path(qrcode_folder: str, category: str, file_name: str) -> str:
    """ Saves the qrcode to the qrcode_folder
    Args:
        qrcode_folder (str): folder where all the qrcodes will be downloaded
        categories (list): the categories list of this row

    Returns:
        str: the path string to save the qrcode
    """
    sub_dir_path = create_subdir(os.path.join(
        qrcode_folder, treat_category(category)))
    qrcode_path = os.path.join(
        sub_dir_path, file_name + '.png')
    return qrcode_path


def get_qrcode(qrcode_folder: str, url: str, category: str) -> None:
    """ Saves the qrcode to the qrcode_folder"
    Args:
        qrcode_folder (str): folder where all the qrcodes will be downloaded
        url (str): the actual url row 
        category (str): the actual category row 
    """
    if is_not_valid_url(url):
        return

    print(f"[Debug] Generating qrcode for page {url}")
    loop = asyncio.get_event_loop()
    qrcode_content = loop.run_until_complete(download_qrcode(url))
    loop.run_until_complete(asyncio.sleep(15))
    qrcode_path = get_qrcode_path(
        qrcode_folder, category, url.replace('https://', '').replace('http://', '').replace('/', '-'))

    save_qrcode(qrcode_path, qrcode_content)
