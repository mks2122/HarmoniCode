import time
from pydub import AudioSegment
from pydub.playback import play as pydub_play

tempo_factor = 1.0  # Default tempo factor

def execute(ast):
    for node in ast:
        if node['type'] == 'play':
            play(node['note'], node['duration'])
        elif node['type'] == 'repeat':
            for _ in range(node['count']):
                execute(node['body'])
        elif node['type'] == 'rest':
            rest(node['duration'])
        elif node['type'] == 'tempo':
            set_tempo(node['bpm'])
        else:
            raise RuntimeError(f"Unknown AST node type: {node['type']}")

def play(note, duration):
    print(f"Playing note: {note} for {duration * tempo_factor} seconds")
    audio1 = AudioSegment.from_mp3(f"./piano-mp3/{note}.mp3")
    adjusted_audio = audio1 + 10  # Adjust volume if necessary
    pydub_play(adjusted_audio)
    time.sleep(duration * tempo_factor)

def rest(duration):
    print(f"Resting for {duration * tempo_factor} seconds")
    time.sleep(duration * tempo_factor)

def set_tempo(bpm):
    global tempo_factor
    tempo_factor = 60.0 / bpm  # Convert BPM to seconds per beat
    print(f"Tempo set to {bpm} BPM, tempo factor: {tempo_factor}")
