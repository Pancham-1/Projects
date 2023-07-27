
max_characters=280
print("-"*40)

tweet = input("Enter your Tweet : ")
character_count=len(tweet)

if character_count < max_characters:
    print(f"That {character_count} characters tweet will work.")
else:
    print(f"That {character_count} characters tweet is {character_count - max_characters} characters too long !!!")

print("-"*40)

# In this exercise I learned to practically use if and else statements by making a character counter.