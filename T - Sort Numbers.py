'''
Problem : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/T
Author : Abdelrahman Mohamed
User: Abdelrahman_JOXIC
Date : 08/07/2024
'''

# take a,b,c and add it to a list
l = list(map(int, input().split()))
l_sorted = l.copy()
l_sorted.sort()

for i in l_sorted:
    print(i)
print()
for i in l:
    print(i)
