class SocialMedia():
    def __init__(self, ownername, platform="facebook", followers=0):
        self.ownername = ownername
        self.platform = platform
        self.followers = followers
        f"Profile for Person-{self.ownername} created."

    def __str__(self):
        return f"{self.ownername} owns a profile in {self.platform} with {self.followers} followers"
