from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.market.get_bazaar() #Get Torn City bazaar data.

print(data)