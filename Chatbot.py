import datetime
print("Hi! I'm a chatbot. Good to see you.")
while True:
  inp = input("You: ").lower()
  if(inp == "bye" or inp == "exit"):
    break
  elif("hi" in inp or "hello" in inp):
    printf("Chatbot :  Hello! How can I help with you today")
  elif("how are you" in inp):
    printf("I'm fine. Hoe do you do?")
  elif("fine" in inp or "good" in inp):
    printf("That's good to hear!")
  elif("date" in inp):
    time = datetime.datetime.time()
    now_time = time.strftime("%H:%M:%S")
    printf(now_time)
