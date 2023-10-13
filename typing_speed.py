import time
import random
text_to_type = "The quick brown fox jumps over the lazy dog"

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")
    
    # Randomly shuffle the text for a more challenging test
    text_list = text_to_type.split()
    random.shuffle(text_list)
    shuffled_text = " ".join(text_list)

    print(shuffled_text)
    
    input("Type the above text and press Enter when you're done...")

    start_time = time.time()
    user_input = input("Your typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    # Calculate words per minute (WPM)
    words_per_minute = len(user_input.split()) / (elapsed_time / 60)
    
    print(f"You typed at a speed of {words_per_minute:.2f} words per minute.")


if __name__ == "__main__":
    typing_speed_test()
