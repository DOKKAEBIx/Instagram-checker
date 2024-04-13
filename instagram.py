def read_txt(file_name):
    """Read data from a text file."""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()
    return data

def get_followers_and_following():
    """Retrieve followers and following data from text files."""
    followers_data = read_txt('followers.txt')
    following_data = read_txt('following.txt')
    followers = [line.strip() for line in followers_data]
    following = [line.strip() for line in following_data]
    return followers, following

def find_unfollowers(followers, following):
    """Find users who are not following back."""
    return list(set(following) - set(followers))

def write_to_file(unfollowers):
    """Write unfollowers to a text file."""
    with open('unfollowers.txt', 'w', encoding='utf-8') as file:
        for username in unfollowers:
            file.write(username + '\n')

def main():
    followers, following = get_followers_and_following()
    unfollowers = find_unfollowers(followers, following)
    write_to_file(unfollowers)
    print("Unfollowers have been saved to 'unfollowers.txt'.")

if __name__ == "__main__":
    main()
