import json


def find_the_word(word):
    with open('Correct_Words.json') as f:
        data = json.loads(f.read())
    for library in data['library']:
        search = library['word']

        if (bool(search == word)) is True:
            part_of_speech = library['part_of_speech']
            break

    return [search, part_of_speech]


def check_word(my_word):
    my_search_result = find_the_word(my_word)[0]
    if (bool(my_search_result == my_word)) is True:
        return True


def true_false_count(search_word, given_word):
    true_count = 0
    false_count = 0

    for i in range(len(search_word)):
        try:
            if (bool(given_word[i] == search_word[i])) is True:
                true_count = true_count + 1
            else:
                false_count = false_count + 1
        except IndexError:
            false_count = false_count + 1
    return [true_count, false_count]


def true_false_comparison(my_list):
    true = my_list[0]
    false = my_list[1]
    if (true >= false) is True:
        return True


def inequality(correct_word, incorrect_word):
    i = 0
    j = 0

    true_count = 0
    false_count = 0
    current_length = max(len(correct_word), len(incorrect_word))
    while i < current_length:
        try:
            if (correct_word[i] == incorrect_word[j]) is True:
                true_count = true_count + 1
                i = i + 1
                j = j + 1
            else:
                i = i + 1
                false_count = false_count + 1
        except IndexError:
            false_count = false_count + 1
            i = i + 1
    return [true_count, false_count]


def my_suggestion(correct_word, word, my_part_of_speech):
    suggestion = input(
        f"Do you mean '{correct_word}'? Because '{word}' does not exist in our library, please type yes or no - ")

    result = False;
    while True:
        if (suggestion == "yes") is True:
            print(f"{correct_word}  is a {my_part_of_speech}")
            result = True
            break
        elif (suggestion == "no") is True:
            print(f"Sorry, '{word}'  does not exist in our library.")
            result = False
            break
        else:
            # print("Please insert a valid response")
            suggestion = input(f"Please, insert a valid response, either yes or no - ")
    return result


def main():
    is_found = 0
    word = input("Please enter your word ")

    try:
        if (check_word(word)) is True:
            my_part_of_speech = find_the_word(word)[1]
            print(f"{word} is a {my_part_of_speech}")
            return
    except UnboundLocalError:
        pass

    with open('Correct_Words.json') as f:
        data = json.loads(f.read())
    for library in data['library']:
        search = library['word']

        part_of_speech = library['part_of_speech']
        if (search != word) is True:
            if (len(search) == len(word)) is True:
                current_list = true_false_count(search, word)

                if (true_false_comparison(current_list)) is True:
                    result = my_suggestion(search, word, part_of_speech)
                    is_found = 1
                    if result is True:
                        break

            if (len(search) != len(word)) is True:
                current_list = inequality(search, word)

                if (true_false_comparison(current_list)) is True:
                    is_found = 1
                    result = my_suggestion(search, word, part_of_speech)
                    if result is True:
                        break

    if (is_found != 1) is True:
        print("We could not find anything similar to your word")


main()

