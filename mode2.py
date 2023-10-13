from __future__ import annotations
import random

from island import Island

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sea_island = []
        self.n_pirates = n_pirates

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        self.sea_island = islands


    def simulate_day(self, crew: int) -> List[Tuple[Island, int]]:
        pirates_count = self.n_pirates
        score = []
        return_list = []
        for pirate in range(pirates_count):
            total_money = 0
            left_crew = crew
            max_score = 0
            max_island = None
            max_crew = 0
            for island in self.sea_island:
                if island.money == 0:
                    continue
                for i in range(left_crew+1):
                    if i > island.marines:
                        continue
                    moneyCollected = min((i*island.money/island.marines),island.money)
                    score = (2*(left_crew-i))+moneyCollected
                    if score > max_score:
                        max_score = score
                        max_island = island
                        max_crew = i
            if max_island is not None:
                max_island.money -= min((max_crew*max_island.money/max_island.marines),max_island.money)
                max_island.marines -= max_crew
                left_crew -= max_crew
            return_list.append((max_island, max_crew))
        return return_list
