
import time
import itertools

class Trafficlight:
    _colour = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [9, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self._colour):
            print(f"\n\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


traffic = Trafficlight()
traffic.running()

