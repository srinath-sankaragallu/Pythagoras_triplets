from math import sqrt

def pyth(a,b):
    res = sqrt( a**2 + b**2 )
    if res.is_integer() :    
        return (a,b,int(res))
    else:    
        return None

def main():
    n = int(input('enter the limit : '))
    if n < 0:
        print(' inavlid input !!!...')
        exit(0)
    result = list()
    for i in range(1,n):
        for j in range(i,n):
            result.append( pyth(i,j))
    result = list(filter( lambda x: x , result))
    print(' number of sets found : ',len(result))
    print(result)

main()
