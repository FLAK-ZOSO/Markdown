#!\usr\bin\env Python3

start = '<!DOCTYPE html><html><head>'
css = '<link rel="stylesheet" href="classes.css">'
body = '</head><body style="background-color: black"><p>'
js = '<script type="text/javascript" src="classes.js"></script>'
end = f'</p>{js}</body></html>'

characters = [
    '***',
    '**',
    '%',
    '*',
    '|',
    '_',
    '/'
]

snippets = [
    '<code class="big">',
    '<code class="bold">',
    '<code class="code">',
    '<code class="italic">',
    '<code class="spoiler">',
    '<code class="underlined">',
    '</code>'
]

associator = dict(zip(characters, snippets))