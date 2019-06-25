cube = lambda x: x*x*x # complete the lambda function 
fibList=[]
def fibonacci(n):
    # return a list of fibonacci numbers
    firstFibNumber = 0
    secondFibNumber = 1
    for i in range (n):
        if i<=1:
            fibList.append(i)
        else:
            fibNumber = firstFibNumber+secondFibNumber
            fibList.append(fibNumber)
            firstFibNumber =secondFibNumber
            secondFibNumber = fibNumber
    return fibList
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))