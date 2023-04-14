import openai
from gtts import gTTS
from pygame import mixer
from pydub import AudioSegment
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.environ["openaiAPI"]

def chat_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=250,
        n=1,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()

def change_pitch(audio, pitch_shift_factor):
    return audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * pitch_shift_factor)})

def play_audio(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.quit()

def apply_audio_effects(audio, pitch_shift_factor):
    # Normaliser le volume
    audio = audio.normalize(headroom=0.1)

    # Fade in et fade out
    audio = audio.fade_in(2000).fade_out(2000)

    # Égalisation
    audio = audio.low_pass_filter(1500).high_pass_filter(500)

    # Compression
    compressed_audio = AudioSegment.silent(duration=100)
    for i in range(0, len(audio), 100):
        chunk = audio[i:i + 100]
        rms = chunk.rms
        if rms > -20:
            gain = -20 - rms
            chunk = chunk + gain
        compressed_audio += chunk

    # Suppression du silence
    audio = audio.strip_silence(silence_len=1000, silence_thresh=-40, padding=100)

    # Ajustement du pitch
    audio = change_pitch(audio, pitch_shift_factor)

    return audio

def text_to_speech(text, lang="fr", slow=False, pitch_shift_factor=1.3):
    # Créer un fichier audio avec gTTS
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save("output.mp3")

    # Charger le fichier audio avec PyDub
    audio = AudioSegment.from_mp3("output.mp3")

    # Appliquer les effets audio
    audio_with_effects = apply_audio_effects(audio, pitch_shift_factor)

    # Sauvegarder le fichier audio modifié
    audio_with_effects.export("output_with_effects.mp3", format="mp3")

    # Jouer le fichier audio avec les effets audio
    play_audio("output_with_effects.mp3")

    # Supprimer les fichiers temporaires
    os.remove("output.mp3")
    os.remove("output_with_effects.mp3")

messages = []

while True:
    user_message = input("Entrez un message (ou 'exit' pour quitter) : ")

    if user_message.lower() == "exit":
        print("Au revoir !")
        break

    messages.append({"role": "system", "content": "Vous parlez avec ChatGPT, un assistant virtuel."})
    messages.append({"role": "user", "content": user_message})

    response_text = chat_gpt(messages)
    messages.append({"role": "assistant", "content": response_text})
    print(response_text)
    text_to_speech(response_text, lang="fr", slow=False, pitch_shift_factor=1.3)

    messages.append({"role": "assistant", "content": response_text})