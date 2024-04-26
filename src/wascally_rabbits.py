"""
In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical
exercise regarding the reproduction of a population of rabbits. He made the 
following simplifying assumptions about the population:

1. The population begins in the first month with a pair of newborn rabbits.
2. Rabbits reach reproductive age after one month.
3. In any given month, every rabbit of reproductive age mates with another
rabbit of reproductive age.
4. Exactly one month after two rabbits mate,they produce one male and one female rabbit.
5. Rabbits never die or stop reproducing.


Given: 
Positive integers n≤40 and k≤5
n = month
k = Length of rabbit's litter

Return: 
The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every
pair of reproduction-age rabbits produces a litter of k rabbit
 pairs (instead of only 1 pair).
"""

def calcule_fibonacci_rabbit_population(n: int, k: int) -> int:
  """
  Calculates the total number of rabbit pairs after n months using dynamic programming.

  Args:
      n: The number of months (0 <= n <= 40).
      k: The number of rabbit pairs produced by each adult pair in a generation (1 <= k <= 5).

  Returns:
      The total number of rabbit pairs after n months.
  """
  lista = [0] * n
  for i in range(0, n):
    if i <= 1:
      lista[i] = 1
    else:
      lista[i] = lista[i - 1] + k * lista[i - 2]
  
  return lista[-1]