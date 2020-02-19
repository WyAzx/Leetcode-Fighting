import queue
class Foo:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.q1.put(0)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.q2.put(0)


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()