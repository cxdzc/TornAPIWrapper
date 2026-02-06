from TornAPIWrapper import TornAPIWrapper, InvalidId

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key.

try:
    data = torn.user.get_profile(user_id=10000000000000000) #Get Torn City user profile data.
    print(data)
except InvalidId:
    print("Woops, that's the wrong ID!")