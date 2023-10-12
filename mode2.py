from __future__ import annotations

from random import random

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


    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        pirates_count = self.n_pirates
        score = []
        for pirate in range(pirates_count):
            total_money = 0
            left_crew = 100
            money_list = []
            # first island
            for island in self.sea_island :
                random_number = random.randint(0, 100)
                moneyCollected = min((random_number*island.money/island.marines),island.money)
                total_money += moneyCollected
                money_list.append((island,moneyCollected))
                left_crew -= random_number
            score.append((2*left_crew)+total_money)




