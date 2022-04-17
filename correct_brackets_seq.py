def clean_input_text(text):
    while '()' in text or r'{}' in text or '[]' in text:
        text = text.replace('()', '')
        text = text.replace(r'{}', '')
        text = text.replace('[]', '')
    return text


def main():
    text = clean_input_text(input())
    if text == '':
        return True
    return False


if __name__ == '__main__':
    print(main())
