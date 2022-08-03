import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("pGBDoAaEpkliVKBOLwjtcmHGc", 
    "xF3g1wrP50b6BlZEd20u4oVfjgH1FGQcuWUzlQO5aUWOufvlhw")
auth.set_access_token("2756992112-Jm8r8XVEWsRbIUg1h0o3U9YLrdV9meyWviM2fUe", 
    "fDWxIF9N7D4wfWSeuoBDFCs5QedblvOX6DRD05KEqGNEh")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")