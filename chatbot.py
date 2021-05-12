import random
import json

import torch
from model import NeuralNet
from pre_processing_utils import bag_of_words, tokenize

from  restura_assistant import ResturaAssistant 
from  restura_api import ResturaApi 


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Google Assistant"
print("Hi, I am at your service! (type 'quit' to exit)")
# ResturaAssistant.speak("Hi, I am at your service")


while True:
    # sentence = "do you use credit cards?"
    # print('You: ')
    # sentence = ResturaAssistant.get_audio()
    sentence = input('You: ')
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                action = intent.get('action')
                if action != None:
                    if action == 'order':
                        ResturaAssistant.executeAction([word for word in sentence if word in ResturaApi.items])
                    else:
                        ResturaAssistant.getData(action)
                else:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    # ResturaAssistant.speak(random.choice(intent['responses']))
                
    else:
        print(f"{bot_name}: Could you rephrase the sentence? I am still in beta.")



