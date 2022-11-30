import time

def recursive(n):
	if (n == 0 or n == 1):
		return n

	return recursive(n - 1) + recursive(n - 2)

def iteration(n):
	fib = [1, 1]
	i = len(fib)
	while i < n:
		fib_old = fib[1]
		fib[1] = fib[0] + fib[1]
		fib[0] = fib_old
		i += 1
	return fib[-1]

start = time.time()
recursive(30)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
recursive(32)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
recursive(35)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
recursive(37)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
iteration(100000)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
iteration(150000)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
iteration(200000)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')

start = time.time()
iteration(400000)
end = time.time()
time_consumed=end-start
print(time_consumed, 's')