import json

with open('intents.json', r) as file:
    intents = json.load(file)

all_words = []
tags = []

# list of patterns and corresponding tags
training_data = []


for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:\
        w = tokenize(pattern)
        all_words.extend(w)
        training_data.append((w, tag))

ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(training_data), "patterns")
print(len(tags), "tags:", tags)
print(len(all_words), "stem words:", all_words)


# create training data
X_train = []
y_train = []
for (pattern_sentence, tag) in training_data:
    # add bag of words for each pattern_sentence as training data
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # no need one-hot encoding for pyTorch CrossEntropyLoss, add labels to training datas
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Hyper-parameters 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # len(dataset) to return the size of the dataset
    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)