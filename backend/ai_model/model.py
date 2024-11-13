import torch
import torch.nn as nn

class TradingModel(nn.Module):
    """A simple neural network model for trading predictions."""
    def __init__(self, input_size, hidden_size=64, output_size=1):
        super(TradingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return self.sigmoid(x)

def load_model(model_path, input_size):
    """Load a pre-trained model from disk."""
    model = TradingModel(input_size)
    try:
        model.load_state_dict(torch.load(model_path))
        model.eval()  # Set the model to evaluation mode
        print(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise
