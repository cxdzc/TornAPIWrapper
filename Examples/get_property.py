from TornAPIWrapper import TornApiWrapper

taw = TornApiWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = taw.get_property(752227, selections=["property", "timestamp"]) #Get Torn City property data.

print(data)