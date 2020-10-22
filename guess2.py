import random 
start = input('please decide a random nunber to start the range: ')
end = input('please decide a random number to finish the range: ')
start = int(start)
end = int(end)

r = random.randint (start,end)
count = 0 
while True:
    count = count + 1
    num = input('please guess a number: ')
    num = int(num)
    if num == r:
        print('Congrats! You are right!')
        print('This is your', count , 'th guess')
        break
    elif num > r:
        print('You are smaller than the answer!')
    elif num < r:
        print('You are bigger than the answer!')
    print('This is your', count , 'th guess')