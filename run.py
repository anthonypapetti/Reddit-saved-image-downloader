import praw

username = input("Username: ")
password = input("Password: ")

reddit = praw.Reddit(username=username, password=password', client_id= 'L5RCDkZeDA9eHw', client_secret='ThGONDxCDy7CrbkYDOajkC2xDbdkkA', user_agent='user',)
print(dir(reddit))

me = reddit.user.me()

for post in me.saved():
    if isinstance(post, praw.models.Submission):
        print(post.url)