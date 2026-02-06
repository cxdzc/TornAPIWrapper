from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key.

data = torn.user.get_bounties() #Get your Torn City user bounty data.

print(data)