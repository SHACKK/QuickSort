import csv
import time
import psutil
import os

#######################################################################################

## 메모리 사용량 확인하는 함수

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")

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

## main() 함수

def main():

    start_time = time.time()

    Number_list = []

    with open("random_list.csv") as random_list:
        reader = csv.reader(random_list, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            Number_list.append(int(row[0]))
    
    result = quick_sort(Number_list)

    ## 출력 하고 싶으면 아래 코드 주석 해제 ##
    #for i in range(1000000):
    #   print(i , " : " , result[i])

    print("TIME : ", time.time() - start_time)
    memory_usage()

#######################################################################################
    
if __name__ == "__main__":
    main()