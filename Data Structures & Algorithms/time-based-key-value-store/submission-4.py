class TimeMap:

    def __init__(self):
        self.time_map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        input_value = (timestamp, value)
        self.time_map[key].append(input_value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        values = self.time_map[key]
        idx = self.binary_search(values, timestamp)
        if idx == -1:
            return ""
        return values[idx][1]
        
    
    def binary_search(self, lst, target):
        """
        Made to search within a list of tuples containing 2 values. (i, v)
        The function will search for the greatest i that is less than or equal to target.
        returns index of the list.
        """
        left, right = 0, len(lst) - 1
        while left < right:
            mid = left + (right - left) // 2
            if lst[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        if lst[left][0] <= target:
            return left
        if left == 0:
            return -1
        return left - 1
