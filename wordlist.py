

import itertools
import os

def generate_combinations(words, min_len, max_len, filename):
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        for length in range(min_len, max_len + 1):
            for combo in itertools.product(words, repeat=length):
                word = "".join(combo)
                f.write(f"{word:<30}\n")  
                count += 1
    return count

if __name__ == "__main__":
    print("=== Advanced Personalized Wordlist Generator ===")

    # Ask personal + extra details
    name = input("Enter Name: ").strip()
    dob = input("Enter DOB (DDMMYYYY): ").strip()
    phone = input("Enter Phone number: ").strip()
    pet = input("Enter Pet name (optional): ").strip()
    fav = input("Enter Favourite word (optional): ").strip()
    college = input("Enter College name (optional): ").strip()
    place = input("Enter Place/City (optional): ").strip()
    lover = input("Enter Lover/Crush name (optional): ").strip()
    nickname = input("Enter Nickname (optional): ").strip()

    # Collect base words
    words = [name, dob, phone, pet, fav, college, place, lover, nickname]
    words = [w for w in words if w]  # remove empty

    # Add variations
    extra = []
    for w in words:
        extra.append(w.lower())
        extra.append(w.upper())
        extra.append(w.title())
        extra.append(w[::-1])         # reversed
        extra.append(w + "123")       # common suffix
        extra.append(w + "@123")
        extra.append("123" + w)
    words.extend(extra)

    # Unique words
    words = list(set(words))

    print(f"\nCollected {len(words)} base words for combinations.")

    # Ask filename
    filename = input("Enter output filename (e.g. mylist.txt): ").strip() or "wordlist.txt"

    # Generate aligned wordlist (1 to 2 words combined)
    total = generate_combinations(words, 1, 2, filename)

    # Show result
    abs_path = os.path.abspath(filename)
    print(f"\n✅ Wordlist saved successfully!")
    print(f"📂 File: {abs_path}")
    print(f"🔢 Total words: {total}")

