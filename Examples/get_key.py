from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key.

data = torn.key.get_log() #Get Torn City key log data.

print(data)