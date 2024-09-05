class Employee:
    name = "Harry"

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1  # Increment i for each character in name
        return i

e = Employee()
print(e.name)
print(len(e))  # Output: 5
