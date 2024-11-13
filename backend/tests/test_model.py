import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from ai_model.train_model import train_model
from ai_model.evaluate_model import evaluate_model
from ai_model.model import AIModel

class TestModel(unittest.TestCase):

    @patch('ai_model.train_model.AIModel')
    def test_train_model(self, mock_ai_model):
        # Mocking the model's train function
        mock_instance = mock_ai_model.return_value
        mock_instance.train.return_value = "Training complete"

        training_data = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [5, 4, 3, 2, 1],
            'label': [0, 1, 0, 1, 0]
        })

        result = train_model(training_data)
        self.assertEqual(result, "Training complete")
        mock_instance.train.assert_called_once_with(training_data)

    @patch('ai_model.evaluate_model.AIModel')
    def test_evaluate_model(self, mock_ai_model):
        # Mocking the model's evaluation function
        mock_instance = mock_ai_model.return_value
        mock_instance.evaluate.return_value = {"accuracy": 0.9, "f1_score": 0.85}

        test_data = pd.DataFrame({
            'feature1': [6, 7, 8],
            'feature2': [2, 3, 1],
            'label': [1, 0, 1]
        })

        metrics = evaluate_model(test_data)
        self.assertEqual(metrics["accuracy"], 0.9)
        self.assertEqual(metrics["f1_score"], 0.85)
        mock_instance.evaluate.assert_called_once_with(test_data)

if __name__ == "__main__":
    unittest.main()
