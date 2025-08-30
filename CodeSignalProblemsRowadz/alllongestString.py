# CHECKED
def all_longest_strings(arr):
    longest_arr = []
    max_len_word = max([len(word) for word in arr])
    longest_arr = [word for word in arr if len(word) == max_len_word]
    return(longest_arr)


if __name__ == "__main__":
    try:
        input_array = ["aba", "aa", "ad", "vce", "aba"]
        print(all_longest_strings(input_array))
    except Exception as e:
        print(e)