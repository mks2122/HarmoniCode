import re

def parse(code):
    tokens = tokenize(code)
    if not tokens:
        raise ValueError("No tokens found. Please check your code.")

    ast = []
    while tokens:
        token = tokens.pop(0)
        if token == 'play':
            ast.append(parse_play(tokens))
        elif token == 'repeat':
            ast.append(parse_repeat(tokens))
        else:
            raise SyntaxError(f"Unexpected token: {token}")
    return ast

def tokenize(code):
    # Tokenizer separates commands, notes, and numbers
    return re.findall(r'\b\w+\b', code)

def parse_play(tokens):
    if not tokens:
        raise SyntaxError("play statement requires a note")
    note = tokens.pop(0)
    return {'type': 'play', 'note': note}

def parse_repeat(tokens):
    if not tokens:
        raise SyntaxError("repeat statement requires a count")
    try:
        count = int(tokens.pop(0))
    except ValueError:
        raise SyntaxError("repeat statement requires a valid integer count")
    
    body = parse_body(tokens)
    return {'type': 'repeat', 'count': count, 'body': body}

def parse_body(tokens):
    body = []
    while tokens:
        token = tokens[0]
        if token == 'play':
            tokens.pop(0)
            body.append(parse_play(tokens))
        elif token == 'repeat':
            tokens.pop(0)
            body.append(parse_repeat(tokens))
        else:
            break  # End of repeat body or unrecognized token
    return body
