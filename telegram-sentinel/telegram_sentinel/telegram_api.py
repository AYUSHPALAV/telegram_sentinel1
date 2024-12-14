import asyncio
import random
from dataclasses import dataclass

@dataclass
class User:
    username: str
    credibility_score: float = None

    def __post_init__(self):
        if self.credibility_score is None:
            self.credibility_score = random.uniform(0, 1)

@dataclass
class Channel:
    name: str

@dataclass
class Message:
    text: str
    user: User
    channel: Channel

class TelegramAPISimulator:
    async def get_new_messages(self, channel):
        """Simulate fetching messages from a Telegram channel"""
        await asyncio.sleep(1)
        return [
            Message(
                "Invest now for guaranteed 1000% returns!", 
                User("scammer123"), 
                channel
            ),
            Message(
                "Legitimate investment opportunity", 
                User("legitimate_business"), 
                channel
            )
        ]