import os
from flask import Flask, jsonify, request, send_from_directory
import instaloader
from flask_cors import CORS
import requests
import time
import threading

app = Flask(__name__)

# Initialize Instaloader
L = instaloader.Instaloader()

# Route to render welcome message

# Enable CORS for all routes
CORS(app)


@app.route('/')
def welcome():
    return "Hello, welcome to Insta Scraper!"


@app.route('/get_profile_info', methods=['GET'])
def get_profile_info():
    username = request.args.get('username')
    try:
        # Download the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Prepare the data to return
        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "profile_pic_url": profile.profile_pic_url,
            "follower_count": profile.followers
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

# Updated route to get username, full name, followers, following, and post count


@app.route('/get_profile_more_details', methods=['GET'])
def get_profile_bio_posts():
    username = request.args.get('username')
    try:
        # Download the profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Prepare the data to return
        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "follower_count": profile.followers,
            "following_count": profile.followees,
            "post_count": profile.mediacount,
            "profile_pic_url": profile.profile_pic_url,
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})


def delete_file_after_delay(filepath, delay):
    time.sleep(delay)
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"File {filepath} deleted.")
    except Exception as e:
        print(f"Error deleting file: {e}")


@app.route('/fetch_instagram_profile', methods=['GET'])
def fetch_instagram_profile():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "username parameter is missing"}), 400

    try:
        # Construct the URL and headers
        url = "https://i.instagram.com/api/v1/users/web_profile_info/?username=" + username

        payload = {}
        headers = {
            'x-ig-app-id': '936619743392459',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        # Define a local directory to store the downloaded profile picture
        local_directory = 'profile_pics'
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # Save the profile picture locally
        # print(response.json())
        # profile_pic_url = response.json().data.user.profile_pic_url

        # get profile pic from response
        profile_pic_url = response.json()["data"]["user"]["profile_pic_url"]

        local_filename = os.path.join(
            local_directory, f"{username}_profile_pic")
        L.download_pic(local_filename, profile_pic_url, 0)

        # Start a thread to delete the file after 10 seconds
        threading.Thread(target=delete_file_after_delay,
                         args=(local_filename, 10)).start()

        # If the request is successful, return the JSON response
        if response.status_code == 200:
            return response.json()
        else:
            return jsonify({"error": f"Failed to fetch profile info. Status code: {response.status_code}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('profile_pics', filename)


if __name__ == '__main__':
    # Bind to 0.0.0.0 and use the port provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
