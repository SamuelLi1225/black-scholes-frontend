# Black-Scholes Option Pricer

A web-based Black-Scholes option pricing calculator with a Python Flask backend and modern web frontend.

## Features

- **Real-time Option Pricing**: Calculate Black-Scholes option prices locally
- **Interactive Interface**: Clean, modern dark theme with floating sidebar
- **Color-coded Results**: Visual heat map for option price ranges
- **Option Greeks**: Calculate Delta, Gamma, Theta, Vega, and Rho
- **Responsive Design**: Professional financial application styling

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Python Backend

```bash
python app.py
```


The API will be available at `http://localhost:5001`

### 3. Open the Frontend


Open `index.html` in your web browser.

## API Endpoints

- `POST /price` - Calculate option price
- `GET /health` - Health check
- `GET /` - API documentation

### Example API Request

```json
{
  "S": 100,     // Stock price
  "K": 105,     // Strike price
  "T": 0.25,    // Time to maturity (years)
  "r": 0.05,    // Risk-free rate
  "sigma": 0.2, // Volatility
  "option_type": "call" // "call" or "put"
}
```

### Example API Response

```json
{
  "price": 2.4556,
  "parameters": {
    "stock_price": 100,
    "strike_price": 105,
    "time_to_maturity": 0.25,
    "risk_free_rate": 0.05,
    "volatility": 0.2,
    "option_type": "call"
  },
  "greeks": {
    "delta": 0.3745,
    "gamma": 0.0234,
    "theta": -0.0456,
    "vega": 0.1234,
    "rho": 0.0567
  }
}
```

## Usage

1. **Start the backend**: Run `python app.py`
2. **Open the frontend**: Open `index.html` in your browser
3. **Enter parameters**: Use the sidebar to input option parameters
4. **Live update**: Results and price table update automatically as you change any parameter—no need to click a button
5. **View results**: Results are color-coded (red=low value, yellow=medium, green=high value)
6. **API errors**: If the backend is not running, a clear error message will appear in the UI

## Files

- `app.py` - Flask API server
- `black_scholes.py` - Black-Scholes calculation functions
- `index.html` - Web frontend
- `styles.css` - CSS styling
- `requirements.txt` - Python dependencies


## UI & Features

- **Live updating**: All calculations and tables update instantly as you change parameters
- **No Calculate button**: The interface is fully reactive
- **API error handling**: If the backend is unavailable, a warning message is shown in the main content area
- **Sidebar/main title alignment**: The sidebar title is visually aligned with the main title for a professional look

## Color Coding

- 🔴 **Red**: Option values < $5 (low value)
- 🟡 **Yellow**: Option values $5-$15 (medium value)
- 🟢 **Green**: Option values > $15 (high value)
- ❌ **Error**: Network or calculation errors
