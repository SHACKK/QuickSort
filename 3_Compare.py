import csv
import time
import psutil
import os
from operator import itemgetter, attrgetter

#######################################################################################

## 메모리 사용량을 리턴하는 함수

def GetMemory():
    # 리턴 단위 MB
    pid = os.getpid()
    mem = psutil.Process(pid)
    mem = mem.memory_info()[0] / 2**20
    return mem

    # rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    # print(f"memory usage: {rss: 10.5f} MB")


#######################################################################################

## 퀵소트 알고리즘

def quick_sort(Number_list):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(Number_list) <= 1:
        return Number_list

    pivot = Number_list[0] # 피벗은 첫 번째 원소
    tail = Number_list[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

#######################################################################################

def work1():
    Number_list1 = []

    with open("random_list_1.csv", "r") as random_list:
        reader = csv.reader(random_list, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            Number_list1.append(int(row[0]))

        start_time = time.time()
        start_memory = GetMemory()
        result_1 = quick_sort(Number_list1)
        end_memory = GetMemory()
        end_time = time.time()
        print("custom QuickSort : ", end_time - start_time)
        print("memory : {:.3f} MB".format(end_memory - start_memory))

def work2():
    Number_list2 = []
    with open("random_list_1.csv", "r") as random_list:
        reader = csv.reader(random_list, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            Number_list2.append(int(row[0]))

        start_time_2 = time.time()
        start_memory_2 = GetMemory()
        result_2 = sorted(Number_list2)
        end_memory_2 = GetMemory()
        end_time_2 = time.time()
        print("sorted function : ", end_time_2 - start_time_2)
        print("memory : {:.3f} MB".format(end_memory_2 - start_memory_2))

## main() 함수

def main():
    work1()
    work2()
#######################################################################################
    
if __name__ == "__main__":
    main()