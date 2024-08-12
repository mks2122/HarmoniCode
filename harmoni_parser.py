import re

def parse(code):
    tokens = tokenize(code)
    print(tokens)
    if not tokens:
        raise ValueError("No tokens found. Please check your code.")

    ast = []
    while tokens:
        token = tokens.pop(0)
        if token == 'play':
            ast.append(parse_play(tokens))
        elif token == 'repeat':
            ast.append(parse_repeat(tokens))
        elif token == 'rest':
            ast.append(parse_rest(tokens))
        elif token == 'set_tempo':
            ast.append(parse_tempo(tokens))
        else:
            raise SyntaxError(f"Unexpected token: {token}")
    return ast

def tokenize(code):
    # Tokenize commands, notes, and numbers, including decimal points for durations
    print(type(code))
    print(code.split())
    # return re.findall(r'\b\w+\b|\d+\.\d+|\d+', code)
    return code.split()
    

def parse_play(tokens):
    if not tokens:
        raise SyntaxError("play statement requires a note")
    note = tokens.pop(0)
    duration = 1.0  # Default duration

    if tokens and (tokens[0].isdigit() or tokens[0].replace('.', '', 1).isdigit()):
        duration = float(tokens.pop(0))

    return {'type': 'play', 'note': note, 'duration': duration}

def parse_repeat(tokens):
    if not tokens:
        raise SyntaxError("repeat statement requires a count")
    try:
        count = int(tokens.pop(0))
    except ValueError:
        raise SyntaxError("repeat statement requires a valid integer count")
    
    body = parse_body(tokens)
    return {'type': 'repeat', 'count': count, 'body': body}

def parse_rest(tokens):
    if not tokens:
        raise SyntaxError("rest statement requires a duration")
    duration = float(tokens.pop(0))
    return {'type': 'rest', 'duration': duration}

def parse_tempo(tokens):
    if not tokens:
        raise SyntaxError("set_tempo statement requires a BPM value")
    bpm = int(tokens.pop(0))
    return {'type': 'tempo', 'bpm': bpm}

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
        elif token == 'rest':
            tokens.pop(0)
            body.append(parse_rest(tokens))
        elif token == 'set_tempo':
            tokens.pop(0)
            body.append(parse_tempo(tokens))
        else:
            break  # End of repeat body or unrecognized token
    return body
