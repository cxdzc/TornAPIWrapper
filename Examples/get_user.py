from torn_api_wrapper import TornApiWrapper

taw = TornApiWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = taw.get_user() #Get Torn City user data.

print(data)