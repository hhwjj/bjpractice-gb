#첫쨋줄 테스트 갯수 C
#둘쨋줄 케이스마다 학생수, 그리고 각 점수

#예제
#5
#5 50 50 70 80 100
#7 100 95 90 80 70 60 50
#3 70 90 80
#3 70 90 81
#9 100 99 98 97 96 95 94 93 91

import sys
input=sys.stdin.readline

C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    #print(case)
    n=case[0]
    sum=0
    net_list=[]
    for k in range(1,n+1):
        sum+=case[k]
        #print(sum)
    #print("sum:",sum)
    avg=sum/n
    #print("average:",avg)
    for k in range(1,n+1):
        if case[k]>avg:
            net_list.append(case[k])
            #print(net_list)
    FP=len(net_list)/n*100
    print("%.3f%%"%FP)

#함수이용해서 만들기
#def Avg(_list:list):

#    length = _list[0]
#    AvgScore = sum(_list[1:]) / length
#    return AvgScore

#def AvgPercent(_list:list,count:int):
#    length = _list[0]
#    a = (count / length)*100
#    return a