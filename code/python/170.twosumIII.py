# Tag:垃圾
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.targets = set()
        self.nums = []
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)

        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        rec = set()
        for n in self.nums:
            if n in rec:
                return True
            rec.add(value-n)
        return False
        