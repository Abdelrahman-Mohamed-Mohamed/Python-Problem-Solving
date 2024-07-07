'''
Problem : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Z
Author : Abdelrahman Mohamed
User: Abdelrahman_JOXIC
Date : 08/07/2024
'''
from math import log
a,b,c,d = map(int,input().split())


# A^B > C^D
if b*log(a) > d*log(c):
    print("YES")
else:
    print("NO")