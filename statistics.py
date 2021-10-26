
def calculateStats(numbers):
    val = len(numbers)
    result = {"max": float('NaN'), "min": float('NaN'), "avg": float('NaN')}
    if val == 0:
        return result
    else:
        result["max"] = max(numbers)
        result["min"] = min(numbers)
        result["avg"] = sum(numbers) / val
        return result


class EmailAlert(object):
    pass


class LEDAlert(object):
    pass


class StatsAlerter(object):
    def __init__(self, maxThreshold, alert):
        self.maxThreshold = maxThreshold
        self.alert = alert
        self.alert[0].emailSent = True
        self.alert[1].ledGlows = False

    def checkAndAlert(self, numbers):
        result = calculateStats(numbers)
        if result["max"] > self.maxThreshold:
            self.alert[0].emailSent = True
            self.alert[1].ledGlows = True

# print(calculateStats([]))
