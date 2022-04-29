from itertools import cycle
from time import sleep


class TrafficLight:
    color = cycle([
        {"signal": "Красный", "duration": 7},
        {"signal": "Желтый", "duration": 2},
        {"signal": "Зеленый", "duration": 5}])

    def running(self):
        light = next(self.color)
        print(f'{light["signal"]} сигнал, пауза {light["duration"]} секунд')
        sleep(light["duration"])


Traffic_Light = TrafficLight()
Traffic_Light.running()
Traffic_Light.running()
Traffic_Light.running()
