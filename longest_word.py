def longest_word(words : list[str]):
  
    if not words:
        return None

    longest = max(words, key=len)
    return longest
        
list_of_words = list(input("Enter a list of words separated by spaces: ").split())
longest = longest_word(list_of_words)
print(f"The longest word is: {longest}")