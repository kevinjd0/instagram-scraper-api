import os
from flask import Flask, jsonify, request
import instaloader

app = Flask(__name__)

# Initialize Instaloader
L = instaloader.Instaloader()

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

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use the port provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
