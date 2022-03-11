"""
gtanslate 1.0: google translate client app
"""

import logging
import argparse
import requests
import time
from common import SUPPORTED_LANGUAGES

log = logging.getLogger(__name__)

GTD_HOST = "http://localhost:8000"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-f",
        type=open,
        metavar="<filename>",
        required=True,
        help="path to input filename to be translated",
    )
    parser.add_argument(
        "-l",
        default="en",
        metavar="<lang>",
        required=True,
        help='output language, can be one of "en", "it" or "de"',
    )

    args = parser.parse_args()
    language = args.l
    if language not in SUPPORTED_LANGUAGES:
        log.error("Unsupported language")
        return
    file = args.f
    with file:
        while True:
            text = file.readline()
            if not text:
                break
            res = requests.get(f'{GTD_HOST}/translate/{language}?text={text}')
            time.sleep(0.25)
            print(res.json()["res"])


if __name__ == "__main__":
    main()
