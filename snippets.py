#!\usr\bin\env Python3
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

start = '<!DOCTYPE html><html><head>'
css = f'<link rel="stylesheet" href="{dir_path}\classes.css">'
body = '</head><body style="background-color: black"><p>'
js = f'<script type="text/javascript" src="{dir_path}\classes.js"></script>'
end = f'</p>{js}</body></html>'

characters = [
    '***',
    '**',
    '$',
    '*',
    '||',
    '_',
]

opening = [
    '<code class="big">',
    '<code class="bold">',
    '<code class="code">',
    '<code class="italic">',
    '<button class="spoiler">',
    '<code class="underlined">',
]

closing = [
    '</code>',
    '</code>',
    '</code>',
    '</code>',
    '</button>',
    '</code>',
]

opener = dict(zip(characters, opening))
closer = dict(zip(characters, closing))