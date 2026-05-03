import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

# Load dataset
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found.")
    raise SystemExit

# Extract genres
genres = sorted({g.strip() for xs in df["Movie_Genre"].dropna().str.split(", ") for g in xs})

# Loading dots
def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Sentiment label
def senti(p):
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

# 🔥 FIXED RECOMMEND FUNCTION
def recommend(genre=None, mood=None, rating=None, n=5):
    d = df.copy()

    # Filter by genre
    if genre:
        d = d[d["Movie_Genre"].str.contains(genre, case=False, na=False)]

    # Filter by rating
    if rating is not None:
        d = d[d["Movie_Rating"] >= rating]

    if d.empty:
        return "No suitable movie recommendations found."

    # Shuffle data
    d = d.sample(frac=1).reset_index(drop=True)

    # Analyze user mood properly ✅
    mp = TextBlob(mood).sentiment.polarity if mood else 0
    need_positive = mp > 0

    out = []

    for _, r in d.iterrows():
        ov = r.get("Movie_Description")

        if pd.isna(ov):
            continue

        pol = TextBlob(ov).sentiment.polarity

        # 🔥 FIXED CONDITION
        if need_positive and pol < 0:
            continue

        out.append((r["Movie_Name"], pol))

        if len(out) == n:
            break

    # 🔥 FALLBACK (important)
    if not out:
        fallback = d.head(n)
        return [(r["Movie_Name"], 0) for _, r in fallback.iterrows()]

    return out

# Show results
def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})")

# Genre input
def get_genre():
    print(Fore.GREEN + "Available Genres: ")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.CYAN}{i}. {g}")
    print()

    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()

        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]

        x = x.title()
        if x in genres:
            return x

        print(Fore.RED + "Invalid input. Please try again.\n")

# Rating input
def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or (s) for 'skip': ").strip()

        if x.lower() == "skip"or "s":
            return None

        try:
            r = float(x)
            if 7.0 <= r <= 9.5:   # 🔥 slightly relaxed
                return r
            print(Fore.RED + "Rating out of range. Try again.\n")

        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

# Main program
print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")

name = input(Fore.YELLOW + "What's your name? ").strip()
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")

print(Fore.BLUE + f"\n🔍 Let's find the perfect movie for you {name}!\n")

genre = get_genre()

mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()

print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
dots()

mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"

print(f"\n{Fore.GREEN}Your mood is {md} (Polarity: {mp:.2f}).\n")

rating = get_rating()

print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
dots()

recs = recommend(genre=genre, mood=mood, rating=rating, n=5)

if isinstance(recs, str):
    print(Fore.RED + recs + "\n")
else:
    show(recs, name)

# Loop for more recommendations
while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()

    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n")
        break

    elif a == "yes":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)

        if isinstance(recs, str):
            print(Fore.RED + recs + "\n")
        else:
            show(recs, name)

    else:
        print(Fore.RED + "Invalid choice. Try again.\n")