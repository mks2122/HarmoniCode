import re

def parse(code):
    tokens = tokenize(code)
    ast = []
    while tokens:
        token = tokens.pop(0)
        if token.startswith('play'):
            ast.append(parse_play(token, tokens))
        elif token.startswith('repeat'):
            ast.append(parse_repeat(token, tokens))
        else:
            raise SyntaxError(f"Unexpected token: {token}")
    return ast

def tokenize(code):
    # Simple tokenizer for demonstration purposes
    return re.findall(r'\b\w+\b', code)

def parse_play(token, tokens):
    note = token.split()[1]
    return {'type': 'play', 'note': note}

def parse_repeat(token, tokens):
    count = int(token.split()[1])
    body = parse_body(tokens)
    return {'type': 'repeat', 'count': count, 'body': body}

def parse_body(tokens):
    # Basic example; in practice, you would need a more sophisticated approach
    body = []
    while tokens and not tokens[0].startswith('repeat'):
        body.append(parse_play(tokens.pop(0), tokens))
    return body
