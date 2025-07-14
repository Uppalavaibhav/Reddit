def fetch_user_data(reddit, username):
    user = reddit.redditor(username)
    comments = list(user.comments.new(limit=50))
    posts = list(user.submissions.new(limit=50))
    return comments, posts
