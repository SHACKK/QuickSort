import random
import csv

f1 = open("./random_list_1.csv", "w", newline="")
count = 1000000

handle = csv.writer(f1)

for i in range(count):
    random_num = random.randint(0, 4294967295)  # 0xffffffff가 10진수로 4294967295이므로 4바이트 내의 랜덤한 정수
    handle.writerow([str(random_num)])

f1.close()

f2 = open("./random_list_2.csv", "w", newline="")
count = 1000000

handle = csv.writer(f2)

for i in range(count):
    random_num = random.randint(0, 4294967295)  # 0xffffffff가 10진수로 4294967295이므로 4바이트 내의 랜덤한 정수
    handle.writerow([str(random_num)])

f2.close()
