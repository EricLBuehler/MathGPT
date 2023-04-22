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

def parse_text_squad(f, output: DatasetCollector):
    obj = json.load(f)
    
    for article in obj["data"]:
        for paragraph in article["paragraphs"]:
            for question in paragraph["qas"]:
                if question["is_impossible"]:
                    for answer in question["plausible_answers"]:
                        text = question["question"].strip()
                        text = text[0].upper() + text[1:]
                        text += " "
                        text += answer["text"].strip()
                        output.append(text)
                    continue

                for answer in question["answers"]:
                    text = question["question"].strip()
                    text = text[0].upper() + text[1:]
                    text += " "
                    text += answer["text"].strip()
                    output.append(text)

output = DatasetCollector()

#SQuAD dataset
with open("train-v2.0.json", "r") as f:
    parse_text_squad(f, output)

with open("dev-v2.0.json", "r") as f:
    parse_text_squad(f, output)

for i in range(1,50):
    for j in range(1,50):
        output.append(f"What is {i}+{j}? {i+j}")
        output.append(f"Compute {i}+{j}? {i+j}")
        output.append(f"{i}+{j} {i+j}")
        output.append(f"{i}+{j}? {i+j}")
        output.append(f"What is {i} plus {j}? {i+j}")
        output.append(f"Compute {i} plus {j}? {i+j}")
        output.append(f"{i} plus {j} {i+j}")
        output.append(f"{i} plus {j}? {i+j}")

        output.append(f"What is {i}-{j}? {i-j}")
        output.append(f"Compute {i}-{j}? {i-j}")
        output.append(f"{i}-{j} {i-j}")
        output.append(f"{i}-{j}? {i-j}")
        output.append(f"What is {i} minus {j}? {i-j}")
        output.append(f"Compute {i} minus {j}? {i-j}")
        output.append(f"{i} minus {j} {i-j}")
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
        output.append(f"Compute {i} by {j}? {i*j}")
        output.append(f"{i} by {j} {i*j}")
        output.append(f"{i} by {j}? {i*j}")

        output.append(f"What is {i}/{j}? {i//j}")
        output.append(f"Compute {i}/{j}? {i//j}")
        output.append(f"{i}/{j} {i//j}")
        output.append(f"{i}/{j}? {i//j}")
        output.append(f"What is {i} divided by {j}? {i//j}")
        output.append(f"Compute {i} divided by {j}? {i//j}")
        output.append(f"{i} divided by {j} {i//j}")
        output.append(f"{i} divided by {j}? {i//j}")

print(f"Number of datapoints: {len(output)}")
print(f"Memory size: {output.get_size()}")
print(f"Maximum line length: {output.max_line()}")

with open("SQuAD.txt", "w+") as f:
    f.write("\n".join(output))