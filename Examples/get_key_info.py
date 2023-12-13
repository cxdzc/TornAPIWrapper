from torn_api_wrapper import TornApiWrapper

taw = TornApiWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = taw.get_key_info() #Get Torn City API key data.

print(data)