from speech import speech_en
from random import choice, randint
import time

# Zorluk seviyeleri
seviyeler = {
    "kolay": ["dairy", "mouse", "computer"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    words = seviyeler.get(level, [])  # Zorluğa göre kelime seçimi
    if not words:
        print("Hatalı zorluk seviyesi.")
        return

    score = 0
    num_attempts = 3  # Kelime başı deneme sayısı

    for _ in range(len(words)):
        random_word = choice(words)
        print(f"Lütfen kelimeyi telaffuz edin: {random_word}")
        recog_word = speech()
        print(recog_word)
        
        if random_word == recog_word:
            print("Doğru!")
            score += 1
        else:
            print(f"Bir yanlışlık var. Kelime: {random_word}")

        time.sleep(2)  # Kelimeler arası bekleme
        
    print(f"Oyun bitti! Skorunuz: {score}/{len(words)}")

# Zorluk seviyesini seçme
selected_level = input("Zorluk seviyesini seçin (kolay/orta/zor): ").lower()
play_game(selected_level)