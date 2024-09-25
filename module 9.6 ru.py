def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            text_ = text[j:i + j + 1]
            yield text_


a = all_variants("abc")
for i in a:
    print(i)
