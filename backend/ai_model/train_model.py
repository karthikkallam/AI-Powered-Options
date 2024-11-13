import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from model import TradingModel
import numpy as np

def train_model(data, input_size, epochs=100, batch_size=32, learning_rate=0.001):
    """Train the trading model with provided data."""
    # Convert data to tensors
    X = torch.tensor(np.array([d['features'] for d in data]), dtype=torch.float32)
    y = torch.tensor(np.array([d['label'] for d in data]), dtype=torch.float32).view(-1, 1)

    # Create DataLoader
    dataset = TensorDataset(X, y)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Initialize model, loss function, and optimizer
    model = TradingModel(input_size)
    criterion = nn.BCELoss()  # Binary Cross Entropy Loss
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Training loop
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for batch_X, batch_y in dataloader:
            optimizer.zero_grad()  # Zero out the gradients
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()  # Backpropagation
            optimizer.step()  # Update weights

            running_loss += loss.item()

        # Print epoch loss
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {running_loss/len(dataloader):.4f}")

    # Save the trained model
    torch.save(model.state_dict(), 'trained_model.pth')
    print("Model training complete and saved as 'trained_model.pth'.")

    return model

if __name__ == "__main__":
    # Example placeholder data for training
    sample_data = [{'features': [0.5, 0.6, 0.8], 'label': 1}, {'features': [0.3, 0.4, 0.5], 'label': 0}]
    trained_model = train_model(sample_data, input_size=len(sample_data[0]['features']))
