# This is very slow, however, it's the first solution I came up with.
# Made helper function to count the "one" bits. Made array of the desired size. Converted each index to binary, then did a count
# on the 1s and passed it to ith slot of the res array.

  def countBits(self, n: int) -> List[int]:
      def count_ones(b):
          counter = 0
          while b:
              counter += b%2
              b = b>>1
          return counter

      res = [0]*(n+1)
      for i in range(len(res)):
          x = format(i,"b")
          count = count_ones(int(x,2))
          res[i] = count
      return res
