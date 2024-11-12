import asyncio,time

async def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        await asyncio.sleep(1)

async def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return print("NOT PRIME")
    return print("PRIME")

async def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        await asyncio.sleep(1)
    print( result)

async def main():
    n = 5
    """tasks = [
        asyncio.create_task(multiplication_table(n)),
        asyncio.create_task(is_prime(n)),
        asyncio.create_task(factorial(n))
    ]"""
    s = time.time()
    await asyncio.gather(multiplication_table(n),is_prime(n),factorial(n))
    elapsed = time.time() - s

    
    
    """for task in tasks:
        await task"""
        
   
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    print("Successful completion")

if __name__ == '__main__':
    
    asyncio.run(main())
