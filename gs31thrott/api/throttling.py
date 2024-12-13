from rest_framework.throttling import UserRateThrottle
from rest_framework.exceptions import Throttled

class JackRateThrottle(UserRateThrottle):
  scope = 'jack'
  
  def throttle_failure(self):
    raise Throttled(detail="HAHAHAH! You are making requests too quickly. Please wait before trying again.")