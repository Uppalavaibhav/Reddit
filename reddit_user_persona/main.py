import argparse
from reddit_client import get_reddit_client
from fetch_user_data import fetch_user_data
from analyze_user_data import analyze_data
from generate_persona import write_persona

def main():
    parser = argparse.ArgumentParser(description='Reddit User Persona Generator')
    parser.add_argument('profile_url', type=str, help='Reddit user profile URL')
    args = parser.parse_args()

    profile_url = args.profile_url
    username = profile_url.rstrip('/').split('/')[-1]
    print(f"Generating persona for: {username}")

    reddit = get_reddit_client()

    comments, posts = fetch_user_data(reddit, username)
    print(f"Fetched {len(comments)} comments and {len(posts)} posts.")

    interests, subreddits, tone, citations = analyze_data(comments, posts)
    write_persona(username, interests, subreddits, tone, citations)

if __name__ == "__main__":
    main()
