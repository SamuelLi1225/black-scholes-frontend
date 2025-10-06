# Deploying Black-Scholes App to Vercel

## Prerequisites
- GitHub account
- Vercel account (free tier available)
- Your code pushed to a GitHub repository

## Project Structure for Vercel

```
black-scholes-frontend/
├── api/
│   ├── index.py          # Serverless function for API
│   └── requirements.txt  # Dependencies for the API
├── index.html           # Frontend application
├── styles.css           # Styles
├── black_scholes.py     # Business logic
├── vercel.json         # Vercel configuration
└── README.md
```

## Deployment Steps

### 1. Push your changes to GitHub
Make sure all the Vercel-specific changes are pushed:

```bash
git add .
git commit -m "Configure for Vercel deployment"
git push
```

### 2. Create a Vercel account
1. Go to [vercel.com](https://vercel.com)
2. Sign up using your GitHub account

### 3. Deploy your project
1. In your Vercel dashboard, click "New Project"
2. Import your GitHub repository: `SamuelLi1225/black-scholes-frontend`
3. Select the branch you want to deploy (e.g., `vercel-deployment`)
4. Vercel will automatically detect the `vercel.json` configuration
5. Click "Deploy"

### 4. Configuration (Automatic)
Vercel will automatically:
- Detect the `vercel.json` configuration
- Build the serverless function from `api/index.py`
- Serve static files (`index.html`, `styles.css`)
- Set up routing to handle both frontend and API requests

## How it works on Vercel

### Serverless Architecture
- **Frontend**: Static files served by Vercel's CDN
- **API**: Serverless functions in the `/api/` directory
- **Routing**: Configured in `vercel.json` to handle both static and dynamic requests

### URL Structure
- **Frontend**: `https://your-app.vercel.app/`
- **API**: `https://your-app.vercel.app/api/price`
- **Health Check**: `https://your-app.vercel.app/api/health`

### Advantages of Vercel
- ✅ **Automatic HTTPS**: SSL certificates included
- ✅ **Global CDN**: Fast loading worldwide
- ✅ **Serverless**: Only pay for what you use
- ✅ **Git Integration**: Auto-deploy on push
- ✅ **Environment Variables**: Easy configuration
- ✅ **Custom Domains**: Add your own domain

## Free Tier Limitations

Vercel's free tier includes:
- 100GB bandwidth per month
- 100 serverless function invocations per day
- 10 deployments per day
- Custom domains supported

## Troubleshooting

### Common Issues:
1. **Import errors**: Make sure `black_scholes.py` is in the root directory
2. **CORS issues**: Already handled with flask-cors
3. **Cold starts**: First request may be slower (normal for serverless)

### Debug Steps:
1. Check Vercel function logs in the dashboard
2. Test the API endpoint directly: `/api/health`
3. Ensure all dependencies are listed in `api/requirements.txt`

## Local Development

To test the Vercel structure locally:

```bash
# Install Vercel CLI
npm install -g vercel

# Run locally
vercel dev
```

This will simulate the Vercel environment on your local machine.

## Environment Variables (if needed)

If you need environment variables:
1. Go to your Vercel project dashboard
2. Settings → Environment Variables
3. Add variables for different environments (Production, Preview, Development)