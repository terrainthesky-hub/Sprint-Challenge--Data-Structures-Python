class RingBuffer:
    def __init__(self, capacity, data = []):
        self.index = 0
        self.capacity = capacity
        self._data = list(data)[-capacity:]

    def append(self, value):
        
        if len(self._data) == self.capacity:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self._data





# class RingBuffer:
#     def __init__(self, capacity):
#         self.storage = []
#         self.capacity = capacity
#         self.oldest = []

#     def append(self, item):
#         if len(self.storage) < 2:
#             return self.storage.append(item), self.oldest.insert(0, item)
            
#         if len(self.storage) >= 2:
#                 return self.storage.insert(0, item), self.storage.remove(self.oldest[2]), self.oldest.pop()

#     def get(self):
#         return self.storage

