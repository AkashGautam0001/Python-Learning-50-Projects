emojis = {
    "love" : "❤️",
    "like" : "👍",
    "hate" : "👎",
    "laugh" : "😂",
    "cry" : "😭",
    "angry" : "😡",
    "code" : "💻",
    "sleep" : "😴"
}

    

def emoji_enhancer(sentence):
    words = sentence.split(" ")
    new_sentence = ""
    # clened_word = word.lower().strip(".,!?")
    for word in words:
        if word in emojis:
            new_sentence += word + emojis[word] + " "
        elif word.endswith((",", ".", "!", "?")):
            new_word = word[:-1]
            if new_word in emojis:
                new_sentence += new_word + emojis[new_word] + word[-1] + " "
            else:
                new_sentence += word + " "
        else:
            new_sentence += word + " "
    return new_sentence

sentence = input("Enter sentences : ")
# updated_message = " ".join(list)
print(emoji_enhancer(sentence))
        



