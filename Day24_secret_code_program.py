# This is the program to translate a message into secret code language.
import random
import string

# Function to generate 3 random lowercase characters
def get_random_string():
    return "".join(random.choices(string.ascii_lowercase, k=3))

st = input("Enter message: ").strip()
words = st.split(" ")
choice = input("1 for Coding or 0 for Decoding: ").strip()
coding = True if choice == "1" else False

nwords = []

for word in words:
    if not word:  # Skip extra spaces
        continue
        
    if coding:
        if len(word) >= 3:
            r1 = get_random_string()
            r2 = get_random_string()
            # Rotate first letter to the end, then wrap with random characters
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    else:
        # Decoding logic
        if len(word) >= 6:  # Since encoded long words always have at least 3+1+3 = 7 chars
            stnew = word[3:-3]  # Strip the 3-letter random prefix and suffix
            stnew = stnew[-1] + stnew[:-1]  # Move the last letter back to the front
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

print("\nResult:")
print(" ".join(nwords))