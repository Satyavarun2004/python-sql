class ResourceManager:
    def __init__(self,resource_name):
        self.resource_name = resource_name

    def __enter__(self):
        print(f"opening resource: {self.resource_name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"closing resource: {self.resource_name}")

    def use_resource(self):
        print(f"using resource: {self.resource_name}")


class NumberIterator:
    def __init__(self,limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

with ResourceManager("MyResource") as resource:
    resource.use_resource()

print("Iterating over numbers:")
number_iterator = NumberIterator(5)
for number in number_iterator:
    print(number)