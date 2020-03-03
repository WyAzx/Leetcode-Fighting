# TAG:多线程
import threading
class DiningPhilosophers:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0
        self.d = [{0, 7, 8}, {0, 8, 9}, {0, 9, 5}, {0, 5, 6}, {0, 6, 7}]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   *actions) -> None:
        with self.c:
            self.c.wait_for(lambda: self.t in self.d[philosopher])
            self.t += philosopher + 5
            self.c.notify_all()
        list(map(lambda func: func(), actions))
        with self.c:
            self.t -= philosopher + 5
            self.c.notify_all()