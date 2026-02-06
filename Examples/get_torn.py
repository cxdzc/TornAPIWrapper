from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key.

data = torn.torn.get_bounties() #Get Torn City bounty data.

print(data)