import time

def time_execution(code):
    start=time.clock()
    result=eval(code)
    stop=time.clock()
    run_time=stop-start
    return result, run_time

def cached_execution(cache, proc, proc_input):
    # format of cache { proc_input1:proc_output1, proc_input2:proc_output2,...}
    if proc_input not in cache:
        cache[proc_input]=proc(proc_input)
    return cache[proc_input]

# Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print cached_execution(cache, factorial, 50)

print "Second time:"
### second execution (should only print out the result)
print cached_execution(cache, factorial, 50)

# Here is a more interesting example using cached_execution
# (do not worry if you do not understand this, though,
# it will be clearer after Unit 6):

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))

cache = {} # new cache for this procedure
# do not try this at home...at least without a cache!
print cached_execution(cache, cached_fibo,100)
