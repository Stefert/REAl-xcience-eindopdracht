import re 

# Dictionary voor patronen.
patterns = { 
   "Do you remember (.*)":"Of course I remember {}", 
   "I feel (.*)":"Why do you feel {}?" 
}

# Dictionary voor veelvoorkomende berichten.
responses = {
  "Hello": ["Hi, how are you?", "Hello!"],
  "I am fine": ["Good to hear!", "Awesome!"]
}

# Functie die het antwoord van de chatbot teruggeeft.
# Dit antwoord komt uit de patterns dictionary,
# de responses dictionary,
# of het is een standaardantwoord.
def get_response(message):
  # Zoek een antwoord in de 'patterns' dictionary
  # en return dit antwoord als het is gevonden.
  for pattern in patterns: 
     match = re.search(pattern,message) 
     if match:
       # hint: patterns[pattern].xxx( ... ) waar xxx een python-functie is.
       # hint: lees hoofdstuk 4.2
       return "Hier komt het antwoord van de chatbot uit de patterns dictionary" 
  
  # Zoek een antwoord in de 'responses' dictionary
  # en return dit antwoord als het is gevonden.
  # Als het niet is gevonden, dan zegt de bot jou na.
  if message in responses:
    # hint: lees hoofdstuk 2.2 en hoofdstuk 3.3
    return random.choice(responses[message])
  else:
    return "I don't understand you."

while True:
  message = input("YOU: ")
  response = get_response(message)
  print("Bot: " + response)











