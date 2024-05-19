from parsers.sakura_kensha_parser import SakuraKenshaParser
import os


def main():
    os.makedirs("data", exist_ok=True)

    SakuraKenshaUrl = "https://www.sakura-kensha.com/futures-portees/"
    SakuraKenshaParser(SakuraKenshaUrl)


if __name__ == "__main__":
    main()
