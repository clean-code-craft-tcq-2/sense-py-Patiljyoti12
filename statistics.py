
def calculateStats(numbers):
  val=len(numbers)
  if val==0:
    return None
  else:
    max_val=max(numbers)
    min_val=min(numbers)
    avg=sum(numbers)/val
    return {"max":max_val,"min":min_val,"avg":avg}


