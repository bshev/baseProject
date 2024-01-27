__author__ = "Brian Shevitski"
__email__ = "brian.shevitski@gmail.com"
__version__ = "0.0.0"
__status__ = "Development"
__date__ = "2024/01/24"

import requests
from loguru import logger


def main():

    URL = "https://www.google.com"
    response = requests.get(URL)

    status = response.status_code
    headers = response.headers

    logger.info(f"Response status: {status}")  # Press ⌘F8 to toggle the breakpoint.
    logger.debug(f" Date: {headers.get('Date')}")
    return response


if __name__ == "__main__":
    main()
