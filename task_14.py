class EvenNumbers:
    def __init__(self, number):
        self.number = number
        self.current = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        result = self.current
        self.current += 2
        self.count += 1
        return result

