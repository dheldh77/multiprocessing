# multiprocessing은 API를 사용해 process spawning 지원
# * process spawning : parent process가 os에 요청해 새로운 child process를 만들어내는 과정
# local concurrency와 remote concurrency를 지원하며, GIL(Global Interpreter Lock)을 효과적으로 우회
# * Local concurrency is defined as "within a system" (e.g. a multi-core CPU), nonlocal concurrency is defined as "between systems"

# Process Pool
# from multiprocessing import Pool

# def f(x):
#     return x * x

# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3])) # [1, 4, 9]

# concurrent.futures.ProcessPoolExecutor
# 호출 프로세스의 실행을 차단하지 않고 task를 백그라운드 프로세스로 실행하는 더 높은 수준의 인터페이스 제공
# Pool과 비교했을 때, 작업을 실행하는 것과 결과를 기다리는 것을 더 쉽게 분리할 수 있음


# import concurrent.futures
# import math

# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419]

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))

# Process Class
# multiprocessing package에서 process는 Process 객체를 만들고 start() 메서드를 호출함으로써 spawn됨
# Process 클래스는 threading.Thread API를 참고

# from multiprocessing import Process
# import os

# def f(name):
#     print(f"parent proecss : {os.getppid()}")
#     print(f"process : {os.getpid()}")
#     print(f"hello, {name}")

# if __name__ == '__main__': # 해당 구문을 사용해서 entry point를 보호하지 않으면 runtime error 발생
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()


# Context and start method
# multiprocessing 프로세스를 시작하는 세가지 방법을 제공합니다.
# 1. spawn
#   - 부모 프로세스는 새로운 python interpreter process를 시작
#   - 자식 프로세스의 run() 메서드를 실행하는데 필요한 리소스만을 상속
#   - 특히, 부모 프로세스의 불필요한 file descriptor와 handle은 상속되지 않음
#   - fork, forkserver를 사용하는 것에 비해 다소 느림
#   - Windows, macOS의 default 설정

# 2. fork
#   - 부모 프로세스는 os.fork()를 사용해 python 인터프리터를 분기
#   - 부모 프로세스의 모든 리소스는 자식 프로세스에 상속

# 3. forkserver
#   - forkserver를 사용하면 서버 프로세스가 시작됨
#   - 새 프로세스가 필요할때마다 상위 프로세스는 서버에 연결해 새 프로세스를 fork하도록 요청
#   - forkserver 프로세스는 단일 스레드이므로 thread safe
#   - 특정 Unix 플랫폼에서만 사용할 수 있음

# 시작 방법 설정
# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     mp.set_start_method('spawn') # set_start_method() 를 두번이상 사용해서는 안됨
#     q = mp.Queue()
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# 컨텍스트 객체 가져오기
# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

