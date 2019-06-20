import pyrithm

fibonacci = pyrithm.algorithm.fibonacci.Fibonacci()

print()
print('Calculate the Fibonacci sequence using recursion and compare '
      'performance when member values are cached. The pyrythim.Fibonacci '
      'class provides two methods: member() and member_slow(). The member() '
      'method features caching and a cache lookup optmiization. The '
      'member_slow() method has no performance optimizations and gets very '
      '')

print('n  nth Fibonacci sequence member')
print('-  -----------------------------')
for n in range(0, 31):
    print(f"{n}  {fibonacci.member(n)}")

##
#
