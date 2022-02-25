#!/usr/bin/python3
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

start = '<!DOCTYPE html>\n<html>\n\t<head>'
css = f'\n\t\t<link rel="stylesheet" href="{dir_path}\classes.css">'
body = '\n\t</head>\n\t<body style="background-color: black">\n\t\t<p>\n\t\t\t'
js = f'\n\t\t<script type="text/javascript" src="{dir_path}\classes.js"></script>'
end = f'\n\t\t</p>{js}\n\t</body>\n</html>'

characters = [
    '***',
    '**',
    '$',
    '*',
    '||',
    '_',
    ']['
]

opening = [
    '<code class="big">',
    '<code class="bold">',
    '<code class="code">',
    '<code class="italic">',
    '<button class="spoiler">',
    '<code class="underlined">',
    '<button class="keyboard">'
]

closing = [
    '</code>',
    '</code>',
    '</code>',
    '</code>',
    '</button>',
    '</code>',
    '</button>'
]

opener = dict(zip(characters, opening))
closer = dict(zip(characters, closing))