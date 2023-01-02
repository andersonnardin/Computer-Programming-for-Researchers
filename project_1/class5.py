#iterator
class my_inclusive_iterator:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high
        
    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.high:
            return self.current
        else:
            raise StopIteration

for i in my_inclusive_iterator(0,10):
    print(i)
    
#generator
def my_inclusive_generator(low, high):
    current = low
    while current <= high:
        yield current
        current += 1
    
for i in my_inclusive_generator(0,10):
    print(i)


    
