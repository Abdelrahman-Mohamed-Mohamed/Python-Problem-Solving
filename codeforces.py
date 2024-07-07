'''
Problem : J. Multiples
Author : Abdelrahman Mohamed
User: Abdelrahman_JOXIC
Date : 08/07/2024
'''

a,b = map(int, input().split())

if a%b == 0 or b%a == 0:
    print('Multiples')
else:
    print('No Multiples')