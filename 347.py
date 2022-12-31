def topKFrequent(nums, k):
  # Create hashmap add all repeating numbers
      d = {}
      for idx in nums:
          if idx not in d:
              d[idx]=1
          else:
              d[idx]+=1

      i = k
      ans = []
      #loop through the keys and find the max value
      while i > 0:
          #note: save the current stake of key along with max value
          mx = 0
          ky = 0
          for key in d:
            if d[key] > mx:
                mx = d[key]
                ky = key
          #append max value to ans array
          ans.append(ky)
          #delete key,value from hashmap
          del d[ky]
          i-=1
      print(ans)
      return ans

topKFrequent([1,1,1,2,2,3], 2)

