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
        self.sea_island += islands
        print(self.sea_island)


    def simulate_day(self, crew: int) -> List[Tuple[Island, int]]:
        pirates_count = self.n_pirates
        score = []
        return_list = []
        for pirate in range(pirates_count):
            total_money = 0
            left_crew = crew
            max_score = 0
            best_island = None
            min_crew = 0
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
                        best_island = island
                        min_crew = i
            if best_island is not None:
                best_island.money -= min((min_crew*best_island.money/best_island.marines),best_island.money)
                best_island.marines -= min_crew
                left_crew -= min_crew
                print(max_score)
                print(best_island.name)
                print(min_crew)
                print(best_island.money)
            return_list.append((best_island, min_crew))
        return return_list
