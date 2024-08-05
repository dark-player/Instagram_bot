'''subscribe infinity trickster '''

from instabot import Bot
import getpass

def login_to_instagram(username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    return bot

def unfollow_everyone(bot):
    followers = bot.get_user_following(bot.user_id)
    for user_id in followers:
        bot.unfollow(user_id)
        username = bot.get_username_from_user_id(user_id)
        print(f"Unfollowed {username}")

def unfollow_names(bot, names):
    followers = bot.get_user_following(bot.user_id)
    for user_id in followers:
        username = bot.get_username_from_user_id(user_id)
        if any(name.lower() in username.lower() for name in names):
            bot.unfollow(user_id)
            print(f"Unfollowed {username}")

def follow_everyone_from_profile(bot, profile_username):
    user_id = bot.get_user_id_from_username(profile_username)
    followers = bot.get_user_following(user_id)
    for user_id in followers:
        bot.follow(user_id)
        username = bot.get_username_from_user_id(user_id)
        print(f"Followed {username}")

def unfollow_everyone_from_profile(bot, profile_username):
    user_id = bot.get_user_id_from_username(profile_username)
    followers = bot.get_user_following(user_id)
    for user_id in followers:
        bot.unfollow(user_id)
        username = bot.get_username_from_user_id(user_id)
        print(f"Unfollowed {username}")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    
    bot = login_to_instagram(username, password)
    
    while True:
        print("\nOptions:")
        print("1. Unfollow everyone")
        print("2. Unfollow names")
        print("3. Follow everyone from a profile")
        print("4. Unfollow everyone from a profile")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            unfollow_everyone(bot)
        elif choice == "2":
            names = input("Enter names to unfollow (comma-separated): ").split(',')
            unfollow_names(bot, [name.strip() for name in names])
        elif choice == "3":
            profile_username = input("Enter the profile username to follow everyone from: ")
            follow_everyone_from_profile(bot, profile_username)
        elif choice == "4":
            profile_username = input("Enter the profile username to unfollow everyone from: ")
            unfollow_everyone_from_profile(bot, profile_username)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
