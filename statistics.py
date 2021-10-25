
def calculateStats(numbers):
  val=len(numbers)
  if val==0:
    return None
  else:
    max_val=max(numbers)
    min_val=min(numbers)
    avg=sum(numbers)/val
    return max_val,min_val,avg

numbers=[1.5, 8.9, 3.2, 4.5]
print(calculateStats(numbers))

