a=(input("Enter your name:"))
print("Hello!",a,"I am an AI CHATBOT")
mood=input("How is your mood today? (good/bad)").lower()
if(mood=="good"):
    print("Wow, Thats very nice!")
elif(mood=="bad"):
    print("No problem,How can I help you to change your mood?")
else:
    print("I know its hard to put feelings into words.")

print("Ok bye!",a)