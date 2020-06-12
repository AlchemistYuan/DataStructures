class SelectionSort():
    def __init__(self):
        return

    def sort(self, array):
        self._sort(array, 0)

    def _sort(self, array, start):
        if start == len(array):
            return
        smallest_index = self._findSmallest(array, start)
        self._swap(array, start, smallest_index)
        self._sort(array, start + 1)

    def _swap(self, array, start, smallest_index):
        array[start], array[smallest_index] = array[smallest_index], array[start]

    def _findSmallest(self, array, start):
        smallest_index = start
        for i in range(start, len(array)):
            if array[i] < array[smallest_index]:
                smallest_index = i
        return smallest_index


def main():
    arr = [6, 3, 4, 5, 7, 2, 8, 1, 0, 9]
    s = SelectionSort()
    s.sort(arr)
    print(arr)

main()
