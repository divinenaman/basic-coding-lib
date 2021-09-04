import sys

sys.stdin = open('input.py.txt','r')
sys.stdout = open('output.py.txt','w')


x = int(input('Enter '))

print(x,"Hola")

sys.stdin.close()
sys.stdout.close()
