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
    app.run(debug=True)
