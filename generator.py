# create a hashtag
def hashtag(text):
    lst = [a.capitalize() for a in text.split()]
    string = ''.join(lst)
    result = f'#{string}'
    return result
