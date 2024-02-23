from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class Sorting(ABC):
    """
    An abstract base class for sorting algorithms.
    """

    @abstractmethod
    def sort(self, data: list[Any]):
        """
         Sorts a list of elements
        :param data: list[Any] the list of elements to be sorted
        :return list[Any]: the sorted list
        """
        pass


class QuickSort(Sorting):
    """
    A class implementing the QuickSort algorithm, a divide-and-conquer sorting algorithm
    """

    def sort(self, data: list[Any]):
        """
        Sorts a list using the QuickSort algorithm.
        :param data: list[Any] lhe list of elements to be sorted
        :return list[Any]: the sorted list
        """
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        less_than_pivot = [x for x in data if x < pivot]
        greater_than_pivot = [x for x in data if x > pivot]
        return self.sort(less_than_pivot) + [pivot] + self.sort(greater_than_pivot)


class BubbleSort(Sorting):
    """
    A class implementing the BubbleSort algorithm
    """

    def sort(self, data: list[Any]):
        """
        Sorts a list using the BubbleSort algorithm
        :param data: list[Any] the list of elements to be sorted
        :return list[Any]: the sorted list
        """

        for i in range(len(data)):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class MergeSort(Sorting):
    """
    A class implementing the MergeSort algorithm
    """

    def sort(self, data: list[Any]):
        """
        Sorts a list using the MergeSort algorithm
        param data: list[Any] the list of elements to be sorted
        :return list[Any]: the sorted list.

        """
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]
        self.sort(left_half)
        self.sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
        return data


class SelectionSort(Sorting):
    """
    A class implementing the SelectionSort algorithm
    """

    def sort(self, data: list[Any]):
        """
        Sorts a list using the SelectionSort algorithm
        :param data: list[Any] the list of elements to be sorted
        :return list[Any]: the sorted list
        """
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data


@dataclass
class SortingManager:
    """
    A class that manages the sorting strategy and performs sorting using the specified strategy.
    """
    sorting_strategy: Sorting

    def set_sorting_strategy(self, sorting_strategy: Sorting):
        """
        Sets the sorting strategy to be used.
        :param sorting_strategy: the sorting strategy to be set
        """
        self.sorting_strategy = sorting_strategy

    def perform_sorting(self, data: list[Any]) -> list[Any]:
        """
        Performs sorting on a list using the current sorting strategy
        :param data: list[Any] the list of elements to be sorted
        :return list[Any]: the sorted list
        """
        return self.sorting_strategy.sort(data)
