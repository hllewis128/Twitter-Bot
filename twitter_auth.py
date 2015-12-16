import tweepy


class TwitterAuth():

    def __init__(self):
        self.config_dict = {
                "consumer_key" :  "",
                "consumer_secret" : "",
                "auth_token" : "",
                "auth_secret" : ""
                }
        with open('consumer.conf', 'r') as config_file:
            for line in config_file:
                line = line.rstrip('\r\n')
                line_array = line.split('=')
                key = (line_array[0]).strip()
                value = (line_array[1]).strip()
                self.config_dict[key] =  value
        config_file.close()

    def get_Auth_Connection(self):
        auth = tweepy.OAuthHandler(self.get_Consumer_Key(), self.get_Consumer_Secret())
        auth.set_access_token(self.get_Auth_Token(), self.get_Auth_Secret())
        return auth

    def get_Consumer_Key(self):
        return self.config_dict["consumer_key"]

    def get_Consumer_Secret(self):
        return self.config_dict["consumer_secret"]

    def get_Auth_Token(self):
        return self.config_dict["auth_token"]

    def get_Auth_Secret(self):
        return self.config_dict["auth_secret"]


