class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Not a non negative int')
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return f"{self.cookies * '🍪'}"

    def deposit(self, n):
        curr_cookies = self.cookies + n
        if curr_cookies > self._capacity:
            raise ValueError('Exceeds the capacity')
        self.cookies = curr_cookies

    def withdraw(self, n):
        curr_cookies = self.cookies - n
        if curr_cookies < 0 :
            raise ValueError('Exhausted all the self.cookies')
        self.cookies = curr_cookies

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,n):
        if n < 0:
            raise ValueError("Capacity can't be negative number")
        self._capacity = n
    
    @property
    def size(self):
        return self.cookies

def main():

    coo = Jar(5)
    coo.deposit(3)
    coo.deposit(2)
    coo.withdraw(4)
    coo.capacity = -10
    print(coo)
    print(coo.capacity)
if __name__ == "__main__":
    main()