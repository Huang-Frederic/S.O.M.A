from parsers.sakura_kensha_parser import SakuraKenshaParser
import os
import time


def main():
    SakuraKenshaUrl = "https://www.sakura-kensha.com/futures-portees/"
    SakuraKenshaParser(SakuraKenshaUrl)


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # while True:
    main()
    # time.sleep(300) # Check every 5 minutes
