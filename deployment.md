# Deployment Guide for Flask App on Render

This guide will walk you through the process of deploying your Flask-based Instagram Scraper API on Render. Render provides a seamless way to deploy web services with automatic builds and deployments.

## Prerequisites

- A [Render](https://render.com/) account (sign up if you don’t have one)
- Your Flask app code hosted in a Git repository (e.g., GitHub)

## Steps to Deploy

### 1. Create a Render Account

If you don't already have a Render account, go to [Render's website](https://render.com/) and sign up.

### 2. Create a New Web Service

1. **After logging in**, click on the **"New +"** button in the top-right corner of the dashboard.
2. Select **"Web Service"** from the dropdown menu.

### 3. Connect Your GitHub Repository

1. Render will prompt you to **connect your GitHub account**. Follow the steps to give Render access to your GitHub repositories.
2. Choose the repository that contains your Flask app. If your repository is private, make sure to grant Render access to it.

### 4. Configure Your Web Service

1. **Choose a Name:** Give your web service a name (e.g., `instagram-scraper-api`).
2. **Select Your Deployment Region:** Choose the region closest to your location for optimal performance.
3. **Instance Type:** Select the **free instance type** to keep your deployment cost-free.

### 5. Build and Deploy Settings

In the **Build and Deploy** section, configure the following settings:

1. **Build Command:**

    ```bash
    pip install -r requirements.txt
    ```

    This command installs all the dependencies listed in your `requirements.txt` file.

2. **Start Command:**

    ```bash
    python app.py
    ```

    This command starts your Flask application.

3. **Auto Deploy:**  
   Enable **Auto Deploy** so that your service redeploys automatically whenever you push changes to the repository.

### 6. Deploy Your Service

Once you’ve configured everything:

1. **Click "Create Web Service"** to start the deployment process.
2. Render will clone your repository, install the dependencies, and start your Flask app.

### 7. Monitor the Deployment

You can monitor the build process and see the logs in real-time. If everything is set up correctly, you should see a message indicating that your service is live.

Here's the part you requested to include in the deployment guide:

### 8. Access Your Flask App

Once the deployment is complete, Render will provide a URL where your Flask app is hosted. The URL will look something like this:

```
https://your-flask-app-name.onrender.com
```

To access your API, you can use the following example URL format:

```
https://your-flask-app-name.onrender.com/get_profile_info?username=instagram_username
```

Replace `your-flask-app-name` with the actual name of your deployed app provided by Render, and `instagram_username` with the Instagram username you want to query.

### Example:

If your Render URL is `https://instagram-scraper-api.onrender.com`, and you want to look up the Instagram profile for `instagram`, your request would look like this:

```
https://instagram-scraper-api.onrender.com/get_profile_info?username=instagram
```

### Note:
If you're unsure of the exact URL, check your Render dashboard under the "Events" or "Logs" section to see the details of your deployment, including the URL assigned to your app.


### 9. (Optional) Enable Continuous Deployment

Since Auto Deploy is enabled, any new commits you push to your repository will automatically trigger a new deployment on Render. This keeps your live service up-to-date with the latest changes.

---

By following these steps, your Flask app should be up and running on Render. The deployment process is straightforward and well-suited for small to medium-sized projects.

Let me know if you need any further assistance!
