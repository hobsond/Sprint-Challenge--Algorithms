# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
    # 01
a)  a = 0
      # o1
    while (a < n * n * n):
      # 01
      a = a + n * n

      # 0
```


```
b)  sum = 0
<!-- o1 -->
    for i in range(n):
    <!-- o[2] -->
      j = 1
      while j < n:
      <!-- o2 -->
        j *= 2
        <!-- o1 -->
        sum += 1
        <!-- o1 -->
        <!-- o(n^2) -->
```

```
c)  def bunnyEars(bunnies):
      <!-- 01 -->
      if bunnies == 0:
      <!-- 01 -->
        return 0
        
<!-- o1 -->
      return 2 + bunnyEars(bunnies-1)

      <!-- o(n) -->
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

