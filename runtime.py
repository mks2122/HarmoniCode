import time

def execute(ast):
    for node in ast:
        if node['type'] == 'play':
            play(node['note'])
        elif node['type'] == 'repeat':
            for _ in range(node['count']):
                execute(node['body'])
        else:
            raise RuntimeError(f"Unknown AST node type: {node['type']}")

def play(note):
    # Placeholder for actual sound generation logic
    print(f"Playing note: {note}")
    time.sleep(0.5)  # Simulate the duration of the note
