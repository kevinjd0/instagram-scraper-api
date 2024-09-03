# Instagram Scraper API

This is a Flask-based API that allows you to retrieve basic information about an Instagram profile, such as the profile picture URL, follower count, and the full name of the user. The API uses the `instaloader` package to fetch this data. No API key is required to use this service.

## Features

- Retrieve profile picture URL
- Get follower count
- Fetch full name of the Instagram user

### Additional Capabilities

Instaloader provides a rich set of features that allow you to fetch much more than just the basic information listed above. For example, you can:

- **Download profile pictures (thumbnails) in various resolutions**
- **Fetch a list of all posts made by the user**
- **Retrieve the captions, hashtags, and comments associated with each post**
- **Download stories, highlights, and IGTV videos (IGTV is now Deprecated) **
- **Access geotags and other metadata related to posts**

You can refer to the [Instaloader documentation](https://instaloader.github.io/) for a comprehensive list of options and capabilities. These can easily be adapted into your `app.py` to extend the functionality of this API.

### Example:

If you want to extend the API to fetch all posts from a user’s profile, you could modify `app.py` to include that functionality using Instaloader’s features. Similarly, you could add endpoints to download stories, depending on your needs.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package installer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kevinjd0/instagram-scraper-api
    cd instagram-scraper-api
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    - **On Windows:**

      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - **On macOS/Linux:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the Flask application, simply run:

```bash
python app.py
```

The application will start a development server on `http://127.0.0.1:5000/`.

## Using the API

Once the server is running, you can access the API at the following endpoint:

```
http://127.0.0.1:5000/get_profile_info?username=instagram_username
```

Replace `instagram_username` with the actual Instagram username you want to query.

### Example Request

```bash
curl "http://127.0.0.1:5000/get_profile_info?username=instagram"
```

### Example Response

```json
{
    "username": "instagram",
    "full_name": "Instagram",
    "profile_pic_url": "https://example.com/profile-pic.jpg",
    "follower_count": 123456789
}
```

## Deployment

For detailed instructions on how to deploy this application on Render, please refer to the [Deployment Guide](./deployment.md).

## No API Key Required

This API does not require an API key or any form of authentication to function.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [Instaloader](https://instaloader.github.io/) for providing a Python interface to Instagram data.
