#!\usr\bin\env Python3
import snippets as s
import sys


def _getText(path: str) -> str:
    with open(f'{path}.txt', 'r') as file:
        return file.read()


def _writeText(path: str, text: str) -> None:
    with open(f'{path}.html', 'w') as file:
        for i in [s.start, s.css, s.js, s.body, text, s.end]:
            file.write(i)


def main(path: str) -> None:
    path = path.removesuffix('.txt')
    txt = _getText(path)

    for i in s.characters:
        for _ in range(txt.count(i)//2):
            txt = txt.replace(i, s.opener[i], 1)
            txt = txt.replace(i, s.closer[i], 1)
    txt = txt.replace('\n', '<br><br>')
    
    _writeText(path, txt)


if (__name__ == '__main__'):
    # D:\Python\Python\Markdown\test.txt
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main(r'D:\Python\Python\Markdown\test.txt')
