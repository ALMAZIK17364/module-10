import threading
import time
class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        threading.Thread.start(self)

    def run(self):
        print(f"{self.name}, на нас напали!\n")
        wariors = 100
        days_cnt = 0

        while wariors > 0:
            time.sleep(1)
            days_cnt += 1
            wariors = wariors - self.power

            print(f"{self.name} сражается {days_cnt}..., осталось {wariors} воинов.")

        print(f"{self.name} одержал победу спустя {days_cnt} дней(дня)!")



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения