import json


class Stack:
    def __init__(self):
        self.top = 0
        self._array = []
    def push(self, element):
        self._array.append(element)
        self.top += 1
        return self
    def pop(self):
        if self.top < 1:
            return None
        self.top -= 1
        return self._array.pop()
    def get_size(self):
        return self.top
    def get_top(self):
        return self._array[-1]
    def clear(self):
        self.top = 0
        self._array = []
        return self
    def __repr__(self):
        return json.dumps(self._array)


class TowerOfHanoi: 
    def __init__(self, start, n):
        self.poles = {"A": Stack(), "B": Stack(), "C": Stack()}
        while n > 0:
             self.poles[start].push(n)
             n -= 1
    def move_disk(self, start, destination):
        disk = self.poles[start].pop()
        self.poles[destination].push(disk)
        output = "moving {} to {}"
        print(output.format(disk, destination))
    def move_tower(self, n, start, temp, destination):
        if n >= 1:
            self.move_tower(n-1, start, destination, temp)
            self.move_disk(start, destination)
            self.move_tower(n-1, temp, start, destination)
        else:
            return None
    def play(self, n, start, temp, destination):
        return self.move_tower(n, start, temp, destination)

if __name__ == "__main__":
    n =int(input("number of disks:"))
    game = TowerOfHanoi("A", n)
    game.play(n, "A", "C", "B")
    print(game.poles["B"])
    
