def transform_text(txt):
    vowel_map = {
        'a': 'i',
        'e': 'o',
        'i': 'u',
        'o': 'a',
        'u': 'e'
    }

    def transform_word(word):
        return ''.join(vowel_map.get(char, char) for char in word)

    words = txt.split()
    transformed_words = [transform_word(word) for word in words]
    return ' '.join(transformed_words)

# Example usage:
# txt = "animals occupdi villages are very important for the ecosystem"
# result = transform_text(txt)
# print(result)
def Human(txt):
    vowel_map = {
            'a': 'i',
            'e': 'o',
            'i': 'u',
            'o': 'a',
            'u': 'e'
        }
    out = []
    for i in txt:
        var = vowel_map.get(i, i)
        out.append(var)

    print(''.join(out))
# Human(txt)

def buble_sort(lstt):
    
    for i in range(0,len(lstt) -1):
        for j in range(0, len(lstt) -i - 1):
            if lstt[j] > lstt[j + 1]:
                lstt[j], lstt[j + 1] = lstt[j + 1], lstt[j]
    print(lstt)

# lstt = [12, 23, 1, 43, 21]
# buble_sort(lstt)


import re

def using_re(txt):
    pattern ='\d{9}'
    pattern = '\((\d{3})\)-(\d{3})-(\d{4})'

    var = re.findall(pattern, txt)
    print(var)

txt1 = """Hello my Number is 123456789 and
            my friend's number is 987654321 our us number is (123)-456-7890"""
# using_re(txt1)

