#TODO: RUN EVERY SCRIPT AND TRY PARAMETERS
# Unit testing?
# - Check every endpoint parameter with all functions created

#TOOD: CREATE MEGA HITLIST FOR 

from torn_api_wrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="REDACTED")

result = torn.user.get_personalstats(user_id=2569585, stat_keys=["attackswon"])

print(f"result\n{result}")

