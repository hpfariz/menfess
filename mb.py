import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("n1GLWLQlfGmkldqNTXZf1w0C6", 
    "7gl6vsSbaQs8PzDAAj4HvSjzP5CgOOC6mlNap4RaSmz7BDFXmm")
auth.set_access_token("1268086140445143040-64A7PRmRSsAYKA7QalTp8T2J8CRX93", 
    "U2gsOH8BD32XEnHbjXRMOUUhUdlL4GKLrecgkuz9hYjxw")

api = tweepy.API(auth)

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("n1GLWLQlfGmkldqNTXZf1w0C6", "7gl6vsSbaQs8PzDAAj4HvSjzP5CgOOC6mlNap4RaSmz7BDFXmm")
# auth.set_access_token("1268086140445143040-64A7PRmRSsAYKA7QalTp8T2J8CRX93", "U2gsOH8BD32XEnHbjXRMOUUhUdlL4GKLrecgkuz9hYjxw")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# isidm = api.list_direct_messages(1, 1)
# for dm in isidm:
#     print(dm.status) 


# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")