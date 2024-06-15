def main():
    filepath = "books/frankenstein.txt"
    file_contents = read_file(filepath)
    word_count = count_words(file_contents)
    character_ocurrences = count_character_ocurrences(file_contents)
    sorted_list_of_dictionaries = create_sorted_list_of_dictionaries(character_ocurrences)
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document")
    print()
    for dictionary in sorted_list_of_dictionaries:
        if dictionary["character"].isalpha():
            print(f"The '{dictionary['character']}' character was found {dictionary['count']} times")
    print("--- End report ---")

def read_file(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(string):
    return len(string.split())

def count_character_ocurrences(string):
    character_occurrences = {}
    for character in string:
        if character.lower() not in character_occurrences:
            character_occurrences[character.lower()] = 1
        else:
            character_occurrences[character.lower()] += 1
    return character_occurrences

def create_sorted_list_of_dictionaries(dictionary):
    sorted_list_of_dictonaries = []
    for character in dictionary:
        sorted_list_of_dictonaries.append({"character":character, "count":dictionary[character]})

    def return_value(dictionary):
        return dictionary["count"]
    sorted_list_of_dictonaries.sort(reverse=True, key=return_value)
    return sorted_list_of_dictonaries

main()
