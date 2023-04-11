import os
import time
from instagramy import InstagramUser
from instagramy.plugins import save_data

def get_user_posts(username):
    user = InstagramUser(username)
    posts = user.posts
    descriptions = []

    for post in posts:
        description = post.caption
        descriptions.append(description)

    return descriptions

def main():
    username = input("Enter the Instagram username: ")
    descriptions = get_user_posts(username)

    print("\nUser post descriptions:")
    for idx, description in enumerate(descriptions):
        print(f"{idx+1}. {description}")

    # Save data to a file if needed
    save_data(descriptions, f"{username}_post_descriptions.txt", mode="w")

if __name__ == "__main__":
    main()




