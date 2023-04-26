# 1 Implementation of selection_sort function:
def selection_sort(numbers: list) -> list:
    n = len(numbers)
    for i in range(n-1, 0, -1):
        max_idx = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    return numbers

# 2 Implementation of binary_search function:
def binary_search(text: list, target: str) -> str:
    left = 0
    right = len(text) - 1
    while left <= right:
        mid = (left + right) // 2
        if text[mid] == target:
            return text[mid]
        elif text[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

# 3 Implementation of HashTable class:
class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return len(key) % self.size
        else:
            raise ValueError("Keys must be either integers or strings.")

    def put(self, key, data):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for i, (k, d) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        hash_key = self.__my_hash(key)
        bucket = self.table[hash_key]
        for k, d in bucket:
            if k == key:
                return d
        return None

# Test selection_sort function
numbers = [3, 6, 2, 8, 1, 9, 4, 7, 5]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)

# Test binary_search function
text = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
target_word = "cherry"
result = binary_search(text, target_word)
print(result)

# Test HashTable class
hash_table = HashTable(5)
hash_table.put(7, "apple")
hash_table.put(3, "banana")
hash_table.put(8, "cherry")
hash_table.put("fig", "date")
hash_table.put("date", "elderberry")
print(hash_table.get(3))
print(hash_table.get(7))
print(hash_table.get("fig"))
print(hash_table.get("apple")) 
