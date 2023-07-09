def to_camel_case(text):
    split_text = text.replace('_', '-').split('-')
    camel_string = split_text[0] + ''.join([word.capitalize() for word in split_text[1:]])
    return camel_string
    