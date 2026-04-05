import time

def show_processing_animation():
    print("Analyzing", end="")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    
def analyze_sentiment(text):
    from textblob import TextBlob
    blob=TextBlob(text)
    print(blob.sentiment)

print("Hi I am the sentiment checking chatbot")
mood=input("How are you?").lower()
#show_processing_animation()
analyze_sentiment(mood)
