from island import Island
from data_structures.bst import BinarySearchTree
from data_structures.heap import MaxHeap
from data_structures.referential_array import ArrayR
from arrayStack import ArrayStack


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.total_crew = crew
        self.islands = islands
        self.ratio_lst = []
        self.island_dic = {}
        self.island_stack = ArrayStack(len(islands))

        for island in islands:
            # Low priority island get high ratio
            ratio_money_marine = island.marines / island.money
            self.ratio_lst.append(ratio_money_marine)
            # Add island to dict with key ratio
            self.island_dic[ratio_money_marine] = island

        self.heap_islands = MaxHeap.heapify(self.ratio_lst)

        # Add island to stack from low priority order
        while self.heap_islands.length > 0:
            # Find the island by ratio
            max_ratio = self.heap_islands.get_max()
            island = self.island_dic[max_ratio]
            self.island_stack.push(island)

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        Use heap with linked dictonary.
        the heap sort the ratio of marine and money. From the max ratio find the island from dicsionary
        """

        crew = self.total_crew
        # idx = 0
        selected_islands = []
        temp_stack = ArrayStack(len(self.islands))

        while not self.island_stack.is_empty():
            # Pop high priprity island from stack
            island = self.island_stack.pop()
            # stroe the island to temporary stack.
            # After teh loop we can reinsert the island object to original stack
            temp_stack.push(island)

            crewToSend = min(island.marines, crew)
            crew -= crewToSend
            # If run out the crew stop iteration
            if crew <= 0:
                break

            returnElem = (island, crewToSend)
            selected_islands.append(returnElem)

        while not temp_stack.is_empty():
            self.island_stack.push(temp_stack.pop())

        return selected_islands

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        money_lst = []
        temp_stack = ArrayStack(len(self.islands))

        for crew in crew_numbers:
            temp_stack.clear()
            current_money = 0
            while not self.island_stack.is_empty():
                island = self.island_stack.pop()
                temp_stack.push(island)

                crewToSend = min(island.marines, crew)
                crew -= crewToSend

                # Clculate how much money Pirate's earn
                current_money += min(island.money * crewToSend / island.marines, island.money)
            # reset stack
            while not temp_stack.is_empty():
                self.island_stack.push(temp_stack.pop())

            money_lst.append(current_money)

        return money_lst

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        island.marines = new_marines
        island.money = new_money
