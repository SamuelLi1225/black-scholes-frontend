from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to the Python path so we can import black_scholes
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from black_scholes import black_scholes, calculate_greeks

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/price', methods=['POST'])
def calculate_price():
    try:
        data = request.get_json()

        # Extract parameters
        S = float(data.get('S', 0))      # Stock price
        K = float(data.get('K', 0))      # Strike price
        T = float(data.get('T', 0))      # Time to maturity
        r = float(data.get('r', 0))      # Risk-free rate
        sigma = float(data.get('sigma', 0))  # Volatility
        option_type = data.get('option_type', 'call').lower()

        # Validate inputs
        if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
            return jsonify({'error': 'All parameters must be positive'}), 400

        if r < 0:
            return jsonify({'error': 'Risk-free rate cannot be negative'}), 400

        if option_type not in ['call', 'put']:
            return jsonify({'error': 'Option type must be "call" or "put"'}), 400

        # Calculate option price
        price = black_scholes(S, K, T, r, sigma, option_type)

        if price is None:
            return jsonify({'error': 'Calculation failed'}), 500

        # Calculate Greeks (optional)
        greeks = calculate_greeks(S, K, T, r, sigma, option_type)

        response = {
            'price': round(price, 4),
            'parameters': {
                'stock_price': S,
                'strike_price': K,
                'time_to_maturity': T,
                'risk_free_rate': r,
                'volatility': sigma,
                'option_type': option_type
            }
        }

        if greeks:
            response['greeks'] = {
                'delta': round(greeks['delta'], 4),
                'gamma': round(greeks['gamma'], 4),
                'theta': round(greeks['theta'], 4),
                'vega': round(greeks['vega'], 4),
                'rho': round(greeks['rho'], 4)
            }

        return jsonify(response)

    except ValueError as e:
        return jsonify({'error': f'Invalid parameter: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'Black-Scholes API is running on Vercel'})

@app.route('/api', methods=['GET'])
def api_info():
    return jsonify({
        'message': 'Black-Scholes Option Pricing API on Vercel',
        'endpoints': {
            '/api/price': 'POST - Calculate option price',
            '/api/health': 'GET - Health check'
        },
        'example_request': {
            'S': 100,
            'K': 105,
            'T': 0.25,
            'r': 0.05,
            'sigma': 0.2,
            'option_type': 'call'
        }
    })

# Vercel expects a handler function
def handler(request):
    return app(request.environ, lambda *args: None)

# For local testing
if __name__ == '__main__':
    app.run(debug=True, port=5001)