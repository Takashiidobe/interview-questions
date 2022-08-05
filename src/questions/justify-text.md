```py
def justify_text(arr, max_width):
    result = []
    curr_words = []
    curr_len = 0
    for word in arr:
        if max_width >= (1 * len(curr_words)) + curr_len + len(word):
            curr_words.append(word)
            curr_len += len(word)
        else:
            spaces_left = max_width - curr_len
            quotient, remainder = divmod(spaces_left, len(curr_words) - 1)
            curr_sentence = ""
            for i, word in enumerate(curr_words):
                if len(curr_words) - 1 == i:
                    curr_sentence += word
                elif i == 0:
                    curr_sentence += word + (' ' * quotient) + (' ' if remainder > i)
                else:
                    curr_sentence += (' ' * quotient) + (' ' if remainder > i) + word
                result.append(curr_sentence)
                curr_words = []

    return result
```
