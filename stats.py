def number_of_words(text):
    words = text.split()
    num_of_words = len(words)
    print(f"Found {num_of_words} total words")
    return num_of_words


def get_characters(text):
    characters = {}
    for char in text:
        if char.upper():
            char = char.lower()
        if char not in characters:
            characters[char] = 1
            continue
        characters[char] += 1
    return characters


def generate_report(filepath, text, characters_dict):
    def sorte(items):
        return items["num"]
    
    characters = []
    
    for key in characters_dict:
        characters.append({"char": key, "num": characters_dict[key]})
    
    characters.sort(reverse=True, key=sorte)       

    print("============ BOOKBOT ===========")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    number_of_words(text)
    print("--------- Character Count -------")
    for i, char in enumerate(characters):
        if characters[i]["char"].isalpha():
            print(f"{characters[i]["char"]}: {characters[i]["num"]}")    
    print("============= END ===============")
    
    return 
