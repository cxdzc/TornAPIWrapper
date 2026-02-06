from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN", request_timeout=25) #Insert your API key.
# OR  request_timeout=(10, 35) / request_timeout=(connect_timeout, read_timeout)

data = torn.user.get_profile(user_id=2561334) #Get Torn City user profile data.

print(data)