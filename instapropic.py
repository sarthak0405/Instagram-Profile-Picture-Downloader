import instaloader

# Create an instance of Instaloader
ig = instaloader.Instaloader()

# Ask for the Instagram username
dp = input("Enter Insta Username:")

try:
    # Download profile picture only
    ig.download_profile(dp, profile_pic_only=True)
    print("Profile picture downloaded successfully!")
except instaloader.exceptions.ProfileNotExistsException:
    print(f"Error: The username '{dp}' does not exist.")
except Exception as e:
    print(f"Error downloading the image: {e}")
