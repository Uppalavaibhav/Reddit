from collections import Counter

def analyze_data(comments, posts):
    comment_texts = [comment.body for comment in comments]
    post_titles = [post.title for post in posts]
    post_subreddits = [post.subreddit.display_name for post in posts]
    comment_subreddits = [comment.subreddit.display_name for comment in comments]

    all_texts = " ".join(comment_texts + post_titles).lower()
    words = all_texts.split()

    common_words = Counter(words).most_common(20)

    stopwords = ['the', 'and', 'to', 'is', 'a', 'of', 'in', 'it', 'for', 'on', 'that', 'with', 'this', 'i', 'you', 'my']
    interests = [word for word, count in common_words if word not in stopwords][:5]

    top_subreddits = Counter(post_subreddits + comment_subreddits).most_common(5)

    if any(word in all_texts for word in ['lol', 'haha', 'bro', 'omg']):
        tone = "Casual"
    else:
        tone = "Formal/Informative"

    citations = []
    for word in interests:
        for post in posts:
            if word in post.title.lower():
                citations.append(f"Interest '{word}' found in post: {post.title} (URL: {post.url})")
        for comment in comments:
            if word in comment.body.lower():
                citations.append(f"Interest '{word}' found in comment: {comment.body[:50]}... (URL: https://reddit.com{comment.permalink})")

    return interests, top_subreddits, tone, citations
