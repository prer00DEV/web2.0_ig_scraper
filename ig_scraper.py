import os
import time
from instagramy import InstagramUser

def get_user_posts(username):
    user = InstagramUser(username)
    posts = user.posts
    descriptions = []
    for post in posts:
        description = post.caption
        descriptions.append(description)

    return descriptions

def main():
    #username = input("Enter the Instagram username: ")
    username = ['breclavsoftball', 'painbusters_most',
                'spectrumpraha', 'joudrsofficial',
                'beaverschomutov', 'zraloci_ledenice',
                'hippos_softball', 'snails_kunovice',
                'tempo_praha']
    descriptions = get_user_posts(username)

    print("\nUser post descriptions:")
    for idx, description in enumerate(descriptions):
        print(f"{idx+1}. {description}")

    # Save data to a csv file
    save_data(descriptions, f"{username}_post_descriptions.txt", mode="w")
    df.to_csv('softball_tymy_posts.csv')

if __name__ == "__main__":
    main()




