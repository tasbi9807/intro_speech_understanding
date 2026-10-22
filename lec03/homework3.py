def words2characters(words):
    characters = []

    for word in words:
        for character in str(word):
            characters.append(character)

    return characters