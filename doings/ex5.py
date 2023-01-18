from dataclasses import dataclass
from time import time

# each social channel has a type
# and the current number of followers
# SocialChannel = tuple[str, int]
@dataclass
class SocialChannel:
    channel_type: str
    followers: int


# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]
@dataclass
class Post:
    message: str
    timestamp: int


def post_to_channel(channel: SocialChannel, message: str) -> None:
    type, followers = channel.channel_type, channel.followers
    print(f"{type} channel: {message}")


def post_to_facebook(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    print(f"{type} channel: {message}")


def post_to_twitter(channel: SocialChannel, message: str) -> None:
    type, followers = channel
    print(f"{type} channel: {message}")


def post_a_message(channel: SocialChannel, message: str) -> None:
    type, followers = channel.channel_type, channel.followers
    if type in ["youtube", "facebook", "twitter"]:
        print(f"{type} channel: {message}")
    # elif type == "facebook":
    #     post_to_facebook(channel, message)
    # elif type == "twitter":
    #     post_to_twitter(channel, message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            if timestamp <= time():
                post_a_message(channel, message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]

    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
