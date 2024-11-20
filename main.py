import re 
import random
import time
import json
import urllib.request



# functie voor het formuleren van de uitkomst van de API.
def getjokes():
  url = 'https://official-joke-api.appspot.com/jokes/random'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  space = (" :                               ")
  setup = result['setup']
  punchline = result['punchline']
  joke = setup + space + punchline
  return joke

# Patroon-Dictionary
patterns = { 
  "Do you remember (.*)":"Of course I remember {}.", 
  "I feel (.*)":"Why do you feel {}?" ,
  "I need (.*)": "You need {}., can i help you?",
  "I dont feel (.*)" : "Im sorry to hear that you dont feel {}., What is wrong?",
  "Because im (.*)" : "Oh i get it now, it is because you are {}.",
  "Can you (.*)"  : "Of course i can {}."
}
  # Responses-Dictionary.
responses = {
  "hello": ["Hi, how are you?", "Hello!, how are you?"],
  "i am fine": ["Good to hear!", "Awesome!"],
  "how about you": ["im  fine, thanks!", "im okay, thanks for asking"],
  "i feel sad" : ["im sorry to hear that, how can i assist you?" , "if you feel down you can always seek help from profesionals"],
  "i need help" : ["how can i help you" , "okay, what can i do for you?"],
  "i feel great" : ["Wel thats amazing to hear!", "thats great!"],
  "i feel happy" : ["Wel thats great to hear!", "thats wonderful!"],
  "no" : ["oh ok, let me know if i can assist you", "ok"],
  "yes" : ["what can i do for you", "how can i help you"],
  "tell me a joke": [getjokes()],
  "how are you" : ["I am fine, how about you", "i'm okay, how are you?"]


} 
# Functie die het antwoord van de chatbot teruggeeft.
def get_response(message):
  for pattern in patterns: 
    match = re.search(pattern,message) 
    if match:
      return patterns[pattern].format(match.group(1))
  if message in responses:
    return random.choice(responses[message])
  else:
    return "i heard you, you said: " + message + ", but i didn't quite understand you." 

#zorgt ervoor dat de responses juist aankomen
while True:
  message = input("YOU: ")
  response = get_response(message)
 
  #laat de chatbot wachten voordat hij praat en voert de response uit
  time.sleep(random.randint(1,2))
  print("Bot: " + response)












