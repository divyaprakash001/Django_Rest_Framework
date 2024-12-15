from rest_framework.throttling import UserRateThrottle,BaseThrottle

class MyThrottling(UserRateThrottle):
  scope = 'mythrottling' 