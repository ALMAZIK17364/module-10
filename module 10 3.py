import threading
import random
import time

lock = threading.Lock()

class Bank:

    def __init__(self):
        self.balance = 0



    def deposit(self):
        lock.acquire()
        for i in range(100):
            a = random.randint(50, 500)
            self.balance += a
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            time.sleep(0.001)
        lock.release()





    def take(self):
        for i in range(100):
            a = random.randint(50, 500)
            print(f"Запрос на {a}")
            if self.balance >= a:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}\n")
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()

        print(f"Пополнение: {a}. Баланс: {self.balance}")



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


