from TornAPIWrapper import TornApiWrapper

taw = TornApiWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = taw.get_faction(selections=["lookup"]) #Get Torn City property data.

print(data)