# a simple chat bot with if else statements shows date and time
import datetime
print("Hi! I'm a chatbot. Good to see you.")
while True:
  inp = input("You: ").lower()
  if(inp == "bye" or inp == "exit"):
    print("It's nice with you. See you again..!")
    break
  elif("hi" in inp or "hello" in inp):
    print("Chatbot :  Hello! How can I help with you today")
  elif("how are you" in inp):
    print("Chatbot : I'm fine. How do you do?")
  elif("fine" in inp or "good" in inp):
    print("Chatbot : That's good to hear!")
#Ask for time, date and day.
  elif("time" in inp):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Chatbot : Now the time is : ",current_time)
  elif("date" in inp):
    now = datetime.datetime.now()
    current_date = now.strftime("%d/%B/%Y")
    print("Chatbot : Todat's date : ",current_date)
  elif("day" in inp):
    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    print("Chatbot : Today's day : ",current_day)
  else:
    printf("You've entered something that is out of focus. Plese try with something else...")
    
