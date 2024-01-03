import re


def main():

    with open(r'story.txt', 'r') as f:
        story = f.read()

    pattern = re.compile(r'<\w+>')
    matches = pattern.findall(story)

    print('Welcome to Mad Libs game\nPlease fill in your word after the colon!')

    for match in matches:
        sub_word = input(f'{match} : ')
        story = re.sub(match, f'{sub_word.upper()}', story)

    print(f'\n{story}')


if __name__ == '__main__':
    main()
