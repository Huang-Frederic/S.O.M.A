from bs4 import BeautifulSoup
import re
import dateparser

from .base_parser import BaseParser
from utils.fetch import fetch_html
from models.sakura_kensha_model import LitterInfo


class SakuraKenshaParser(BaseParser):
    def __init__(self, url):
        self.url = url
        self.html = fetch_html(self.url)
        self.litters = self.parse(self.html)

        self.display_litters()

    def parse(self, html):
        # Parse the html and return a list of elements
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find_all(class_="elementor-widget-text-editor")
        elements = [content.get_text(strip=True) for content in contents]

        # Parse the elements into a list of LitterInfo objects (the )
        litters = []
        # All the informations of a litter is in 3 consecutive elements
        for i in range(0, len(elements), 3):
            try:
                # Parse parents
                parents = elements[i].split(" x")
                if len(parents) != 2:
                    continue
                father, mother = parents

                # Parse pedigree
                pedigree_match = re.search(
                    r"\((.*?)\)", elements[i+1])
                pedigree = pedigree_match.group(1) if pedigree_match else None

                # Parse Litter quantity
                litter_match = re.search(r"(\d+) chiots", elements[i+2])
                litter = int(litter_match.group(1)) if litter_match else 0

                # Parse birthdate
                birthdate_match = re.search(
                    r"(\d{1,2}(?:er)? \w+ 2024)", elements[i+2])
                birthdate = dateparser.parse(
                    birthdate_match.group(1)).date()

                # Parse expected races
                expected_race = [0, 0, 0]  # [roux, sésame, n&f]
                if "roux" in elements[i+2]:
                    expected_race[0] = 1
                if "sésame" in elements[i+2]:
                    expected_race[1] = 1
                if "n&f" in elements[i+2]:
                    expected_race[2] = 1

                # Create LitterInfo object
                litters.append(LitterInfo(father, mother, pedigree,
                               litter, birthdate, expected_race))
            except Exception as e:
                print(f"Error parsing litter from Sakura Kensha: {e}")
        return litters

    def display_litters(self):
        for litter in self.litters:
            print(litter)
