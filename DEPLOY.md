# Deploying Black-Scholes App to Render

## Prerequisites
- GitHub account
- Render account (free tier available)
- Your code pushed to a GitHub repository

## Deployment Steps

### 1. Push your changes to GitHub
Your code should already be in a GitHub repository. Make sure all the latest changes are pushed:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push
```

### 2. Create a Render account
1. Go to [render.com](https://render.com)
2. Sign up using your GitHub account

### 3. Deploy your web service
1. In your Render dashboard, click "New +" and select "Web Service"
2. Connect your GitHub repository containing this project
3. Configure the service:
   - **Name**: black-scholes-app (or any name you prefer)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free (or upgrade if needed)

### 4. Environment Variables
Render will automatically detect the `render.yaml` file and use its configuration. No manual environment variables needed.

### 5. Deploy
1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies from requirements.txt
   - Start your Flask application
   - Provide you with a public URL

## How it works

Your Flask app now serves both:
- **Frontend**: The HTML interface at the root URL (`/`)
- **API**: The Black-Scholes calculation endpoint at (`/price`)

The frontend will automatically use relative URLs, so it works both locally and in production.

## Accessing your deployed app

Once deployment is complete, you'll get a URL like:
`https://your-app-name.onrender.com`

- Visit this URL to see your Black-Scholes calculator
- The API endpoint will be at: `https://your-app-name.onrender.com/price`

## Local development

To run locally, you can still use:
```bash
python app.py
```

The app will run on `http://localhost:5001` and serve both frontend and API.

## Troubleshooting

If deployment fails:
1. Check the build logs in Render dashboard
2. Ensure all files are committed to your repository
3. Verify `requirements.txt` includes all necessary dependencies
4. Check that your Python version is compatible (3.11+ recommended)

## Free tier limitations

Render's free tier:
- Apps sleep after 15 minutes of inactivity
- 750 hours per month of runtime
- Public repositories only
- Slower cold starts

For production use, consider upgrading to a paid plan.