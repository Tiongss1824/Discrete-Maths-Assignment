from pydub import AudioSegment
from pydub.generators import Sine
import random

# Define a simple scale (C major scale for simplicity)
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88,
}

# Define a simple graph for transitions
graph = {
    "C": ["D", "E", "G"],
    "D": ["E", "F", "A"],
    "E": ["F", "G", "B"],
    "F": ["G", "A", "C"],
    "G": ["A", "B", "D"],
    "A": ["B", "C", "D"],
    "B": ["C", "D", "E"],
}

# Function to generate a sine wave for a note
def generate_note(note, duration_ms=300):
    frequency = notes[note]
    return Sine(frequency).to_audio_segment(duration=duration_ms)

# Function to generate a chord (3 notes stacked)
def generate_chord(note, duration_ms=300):
    frequencies = [notes[note], notes["C"], notes["E"]]  # Example for C major chord
    chord = AudioSegment.silent(duration=duration_ms)
    for freq in frequencies:
        chord = chord.overlay(Sine(freq).to_audio_segment(duration=duration_ms))
    return chord

# Function to create a random melody using graph traversal
def generate_melody(start_note, length=8):
    melody = [start_note]
    current_note = start_note
    for _ in range(length - 1):
        next_note = random.choice(graph[current_note])
        melody.append(next_note)
        current_note = next_note
    return melody

# Generate the melody
melody = generate_melody("C", 100)

# Create the audio sequence
audio = AudioSegment.silent(duration=0)

for i, note in enumerate(melody):
    # Randomize note length (short or long note durations)
    duration = random.choice([200, 300, 400])
    
    # Add a chord every 4th note to provide harmony
    if i % 4 == 0:
        audio += generate_chord(note, duration)
    else:
        audio += generate_note(note, duration)

# Export the audio
audio.export("Anime-30seconds_v2.wav", format="wav")
