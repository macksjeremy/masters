import praw
def init():
    reddit = praw.Reddit(
        client_id="FEyMTKPEt9gdL3PjaRtmBw",
        client_secret="K25Ika19-XhYHGvLHGvsF8NDuZy9Qg",
        user_agent= "Web:SimulatedScraper:0.0.0 by u/macksjapi",
        username="macksjapi",
        password="PublicAccount")
    return reddit