from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.user.get_profile(user_id=2561334) #Get Torn City user profile data.

print(data)