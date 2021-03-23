import praw


reddit = praw.Reddit(
    client_id="3gt3Cgaiz2W9zA",
    client_secret="Tebl2KXTSYmP8NuqBqjor-dJHrPMwA",
    password="********",
    user_agent="testscript by u/sanzid-olioul",
    redirect_uri="http://localhost:8000",
    username="sanzid-olioul",
)

headlines = set()

for submission in reddit.redditors.new(limit=None):
    print(submission)

# print(reddit.user.me())