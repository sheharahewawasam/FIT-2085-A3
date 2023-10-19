from island import Island
from data_structures.bst import BinarySearchTree
from data_structures.heap import MaxHeap
from data_structures.referential_array import ArrayR
from arrayStack import ArrayStack

class Mode1Navigator:
    """
    Mode1Navigator is a class that represents a navigator responsible for selecting islands
    for exploration based on a specific strategy. The strategy involves prioritizing islands
    with the highest ratio of marines to money and allocating available crew members to these
    islands accordingly.

    Attributes:
        total_crew (int): The total number of crew members available for exploration.
        sea_islands (list[Island]): A list of Island objects representing the available islands.
        ratios (list[float]): A list of island ratios (marines to money) for prioritization.
        islandDictionary (dict[float, Island]): A dictionary mapping ratios to islands.
        islandStack (ArrayStack): A stack for managing islands based on their priority.

    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Initializes a Mode1Navigator with a list of islands and a crew size.

        Args:
            islands (list[Island]): A list of Island objects to explore.
            crew (int): The total number of crew members available.

        """
        self.total_crew = crew
        self.sea_islands = islands
        self.ratios = []
        self.islandDictionary = {}
        self.islandStack = ArrayStack(len(islands))

        for island in islands:
            # Low priority island gets high ratio
            ratio_money_marine = island.marines / island.money
            self.ratios.append(ratio_money_marine)
            # Add island to the dictionary with key ratio
            self.islandDictionary[ratio_money_marine] = island

        self.islandsHeap = MaxHeap.heapify(self.ratios)

        # Add islands to the stack in a low-priority order
        while self.islandsHeap.length > 0:
            # Find the island by ratio
            maxRatio = self.islandsHeap.get_max()
            island = self.islandDictionary[maxRatio]
            self.islandStack.push(island)

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Select and allocate crew to islands based on their ratio of marines to money.

        Returns:
            list[tuple[Island, int]]: A list of tuples representing the selected islands
            and the allocated crew for each.

        """
        crew = self.total_crew
        islandsSelected = []
        tempStack = ArrayStack(len(self.sea_islands))

        while not self.islandStack.is_empty():
            island = self.islandStack.pop()
            # Store the island in a temporary stack.
            # After the loop, we can reinsert the island object into the original stack.
            tempStack.push(island)

            crewToSend = min(island.marines, crew)
            if crew < crewToSend:
                returnElem = (island, crew)
                islandsSelected.append(returnElem)
                break
            crew -= crewToSend

            returnElem = (island, crewToSend)
            islandsSelected.append(returnElem)

        while not tempStack.is_empty():
            self.islandStack.push(tempStack.pop())

        return islandsSelected

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Select and allocate crew to islands based on a list of crew numbers.

        Args:
            crew_numbers (list[int]): A list of crew sizes to allocate to islands.

        Returns:
            list[float]: A list of the total money earned for each allocation.

        """
        moneyList = []
        tempStack = ArrayStack(len(self.sea_islands))

        for crew in crew_numbers:
            tempStack.clear()
            current_money = 0
            while not self.islandStack.is_empty():
                island = self.islandStack.pop()
                tempStack.push(island)

                crewToSend = min(island.marines, crew)
                crew -= crewToSend

                current_money += min(island.money * crewToSend / island.marines, island.money)

            while not tempStack.is_empty():
                self.islandStack.push(tempStack.pop())

            moneyList.append(current_money)

        return moneyList

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Update the information for a specific island.

        Args:
            island (Island): The Island object to be updated.
            new_money (float): The new amount of money available on the island.
            new_marines (int): The new number of marines stationed on the island.

        """
        island.marines = new_marines
        island.money = new_money
