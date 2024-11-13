from flask import Flask
from flask_cors import CORS
from api.routes.trading_routes import trading_blueprint
from api.routes.data_routes import data_blueprint
import config

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for all routes

# Register Blueprints
app.register_blueprint(trading_blueprint, url_prefix='/api/trading')
app.register_blueprint(data_blueprint, url_prefix='/api/data')

# Load configuration
app.config.from_object(config)

@app.route('/')
def home():
    return "Welcome to the AI-Powered Options Trading API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
