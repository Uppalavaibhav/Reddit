import os

def write_persona(username, interests, subreddits, tone, citations):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{username}_persona.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"User Persona for: {username}\n\n")
        f.write(f"Top Interests: {', '.join(interests)}\n\n")
        f.write(f"Preferred Subreddits: {', '.join([sub for sub, count in subreddits])}\n\n")
        f.write(f"Content Tone: {tone}\n\n")
        f.write("Citations:\n")
        for cite in citations:
            f.write(f"- {cite}\n")

    print(f"Persona written to {filename}")
