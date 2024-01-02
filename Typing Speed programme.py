import time
import random

def randomText():
    words =""
    with open("thousandwords.txt", "r") as f:
        words = f.read().split()
        random_words = ' '.join(random.sample(words, k=20))
        return random_words

def test():
    print("Welcome to Typing Speed Test!")
    input("Press Enter when you are ready to start...")
    output = randomText()
    print("\nType the following:")
    print(output)
    input("Press Enter to start typing...")
    start_time = time.time()
    typed_text = input("\nType here: ")
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_typed = len(typed_text.split())
    wpm = int((words_typed / elapsed_time) * 60)
    print(f"\nYour typing speed: {wpm} WPM")
    correct_words = sum(1 for a, b in zip(output.split(), typed_text.split()) if a == b)
    accuracy = (correct_words / len(output.split())) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    test()
