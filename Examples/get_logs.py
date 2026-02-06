from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key.

data = torn.user.get_log() #Get Torn City user log data.

print(data)