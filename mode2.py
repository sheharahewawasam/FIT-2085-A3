from __future__ import annotations
import random
from typing import List, Tuple

from island import Island

class Mode2Navigator:
    """
    Mode2Navigator is a class that simulates the actions of pirates who explore islands to maximize their profit.
    The navigator uses a heuristic strategy to select islands for exploration and allocate crew members to them.

    Attributes:
        sea_island (list[Island]): A list of Island objects representing the available islands.
        n_pirates (int): The number of pirates available for exploration.

    """

    def __init__(self, n_pirates: int) -> None:
        """
        Initializes a Mode2Navigator with the number of pirates.

        Args:
            n_pirates (int): The number of pirates available for exploration.

        """
        self.sea_island = []
        self.n_pirates = n_pirates

    def add_islands(self, islands: list[Island]) -> None:
        """
        Adds a list of islands to the navigator's available islands.

        Args:
            islands (list[Island]): A list of Island objects to add to the available islands.

        """
        self.sea_island += islands

    def simulate_day(self, crew: int) -> List[Tuple[Island, int]]:
        """
        Simulates a day of pirate exploration, allocating crew members to islands to maximize profit.

        Args:
            crew (int): The total crew members available for exploration.

        Returns:
            List[Tuple[Island, int]]: A list of tuples representing the selected islands and the allocated crew
            for each island exploration.

        """
        pirates_count = self.n_pirates
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

                for i in range(left_crew + 1):
                    if i > island.marines:
                        continue
                    money_collected = min((i * island.money / island.marines), island.money)
                    score = (2 * (left_crew - i)) + money_collected

                    if score > max_score:
                        max_score = score
                        best_island = island
                        min_crew = i

            if best_island is not None:
                best_island.money -= min((min_crew * best_island.money / best_island.marines), best_island.money)
                best_island.marines -= min_crew
                left_crew -= min_crew

            return_list.append((best_island, min_crew))

        return return_list
