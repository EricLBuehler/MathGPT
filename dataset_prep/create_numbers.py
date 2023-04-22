import json
import sys

class DatasetCollector:
    def __init__(self) -> None:
        self._data = []
        self.idx = 0
        self.max = 0

    def append(self, o: object) -> None:
        self._data.append(o)
        self.max = max(len(o), self.max)

    def __iter__(self):
        return self
    
    def __next__(self):
        self.idx += 1 
        if self.idx > len(self):
            raise StopIteration
        return self._data[self.idx-1]

    def max_line(self) -> int:
        return self.max

    def __len__(self) -> int:
        return len(self._data)
    
    def get_size(self) -> int:
        return sys.getsizeof(self) + sys.getsizeof(self._data) + sys.getsizeof(self.idx) + sys.getsizeof(self.max)


output = DatasetCollector()

for i in range(1,200):
    for j in range(1,200):
        output.append(f"What is {i}+{j}? {i+j}")
        output.append(f"Compute {i}+{j}? {i+j}")
        output.append(f"{i}+{j} {i+j}")
        output.append(f"{i}+{j}? {i+j}")
        output.append(f"What is {i} plus {j}? {i+j}")
        output.append(f"Compute {i} plus {j}: {i+j}")
        output.append(f"{i} plus {j}? {i+j}")

        output.append(f"What is {i}-{j}? {i-j}")
        output.append(f"Compute {i}-{j}? {i-j}")
        output.append(f"{i}-{j} {i-j}")
        output.append(f"{i}-{j}? {i-j}")
        output.append(f"What is {i} minus {j}? {i-j}")
        output.append(f"Compute {i} minus {j}: {i-j}")
        output.append(f"{i} minus {j}? {i-j}")

        output.append(f"What is {i}*{j}? {i*j}")
        output.append(f"Compute {i}*{j}? {i*j}")
        output.append(f"{i}*{j} {i*j}")
        output.append(f"{i}*{j}? {i*j}")
        output.append(f"What is {i} times {j}? {i*j}")
        output.append(f"Compute {i} times {j}? {i*j}")
        output.append(f"{i} times {j} {i*j}")
        output.append(f"{i} times {j}? {i*j}")
        output.append(f"What is {i} by {j}? {i*j}")
        output.append(f"Compute {i} by {j}: {i*j}")
        output.append(f"{i} by {j}? {i*j}")

        output.append(f"What is {i}/{j}? {i//j}")
        output.append(f"Compute {i}/{j}? {i//j}")
        output.append(f"{i}/{j} {i//j}")
        output.append(f"{i}/{j}? {i//j}")
        output.append(f"What is {i} divided by {j}? {i//j}")
        output.append(f"Compute {i} divided by {j}: {i//j}")
        output.append(f"{i} divided by {j}? {i//j}")

print(f"Number of datapoints: {len(output)}")
print(f"Memory size: {output.get_size()}")
print(f"Maximum line length: {output.max_line()}")

with open("numbers.txt", "w+") as f:
    f.write("\n".join(output))