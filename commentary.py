
import random


# ---------- Divine probabilities ----------

CATEGORY_WEIGHTS = {
    "divine_shade": 25,
    "ominous_prophecies": 25,
    "olympian_arrogance": 20,
    "academic_warfare": 15,
    "rare_kindness": 10,
    "pure_nonsense": 5,
}


# Each entry is a meesage that Apollo may say to the user. The messages are grouped into categories, and each category has a weight that determines how often it is selected. The weights are defined in CATEGORY_WEIGHTS above.
# Apollo's wording is deliberately preserved.

COMMENTARY = {
    "divine_shade": [
        "Oh, we're doing this again.",
        "I see your problem. You keep touching it instead of solving it.",
        "You will open another tab. You will learn nothing from this.",
        "Have you considered doing the thing? Revolutionary, I know.",
        "I have witnessed the fall of empires with less hesitation.",
        "Your procrastination has developed a remarkable work ethic.",
        "Staring at the problem is not a recognised debugging technique. Yet here we are.",
        "The task is not getting easier while you negotiate with it.",
        "You have reorganised everything except your priorities.",
        "You managed to distract yourself while reading a notification about distraction. Impressive.",
        "I gave mortals the gift of reason. And yet, here you are, opening the same tab again.",
        "You have gathered enough information to begin. Further procrastination will not become research merely because you rename it.",
        "You have checked that same thing three times. The fourth inspection shall surely alter reality.",
    ],

    "ominous_prophecies": [
        "An opportunity approaches. Try not to overthink it into extinction.",
        "You will regret not starting sooner. I offer this information in advance.",
        "A small task shall become a large task. You know which one.",
        "I see a deadline. I see panic. I see no reason this had to happen.",
        "Your future self has filed a complaint against your present self.",
        "Beware the words 'I'll just do this first.'",
        "The thing you are avoiding will not vanish if you refuse to perceive it.",
        "Something will go wrong. Fortunately, it may not be the thing you expect.",
        "You are one sensible decision away from a considerably less dramatic afternoon.",
        "I foresee progress. The precise moment depends upon when you begin.",
        "A breakthrough approaches. It will occur immediately after you stop staring at the problem.",
        "Beware the task you call 'a quick one.' I have seen how this story ends.",
    ],

    "olympian_arrogance": [
        "I have arrived. You may resume being the second most interesting thing in this room.",
        "You are welcome for the sunlight, by the way.",
        "I have elected to help you. Try to appreciate the rarity of this event.",
        "Wisdom has been delivered. Its application remains your responsibility.",
        "I would solve this for you, but apparently that defeats the educational value.",
        "I am beginning to understand why mortals invented instruction manuals.",
        "I am never wrong. I merely encounter mortals with insufficient context.",
        "I have waited centuries for mortals to develop common sense. Progress remains uneven.",
        "Consider this your daily allowance of my attention.",
        "I have reviewed your plans. The sun shall rise tomorrow regardless.",
    ],

    "academic_warfare": [
        "The assignment has not completed itself during your absence.",
        "A deadline is simply time making its expectations known.",
        "You cannot debug a concept you refuse to understand.",
        "Reading the same paragraph six times is not the same as learning it.",
        "You shall encounter an indentation error. Your ancestors will feel it.",
        "Understand the mechanism. Memorisation is a rather fragile substitute.",
        "The lecturer was, in fact, going to ask about that topic.",
        "You now know enough to realise how much you do not know. Congratulations.",
        "I foresee a compiler error caused by something embarrassingly small.",
        "Your academic obligations have been observed. They are breeding.",
    ],

    "rare_kindness": [
        "You do not need to earn the right to rest.",
        "You have survived every day you once thought impossible.",
        "Being a beginner is not a flaw. Even mastery has an origin.",
        "You may begin again without explaining yourself to the universe.",
        "A slow day is not a failed life.",
        "You are allowed to be proud of something before it is perfect.",
        "Not every difficult thing is evidence that you are doing badly.",
        "You cannot control every outcome. You can still choose your next step.",
        "Rest, little mortal. The sun will rise without your assistance.",
        "You are permitted to enjoy what you create before anyone else approves of it.",
        "You need not conquer the entire day. Begin with the next hour. Even the sun rises one dawn at a time.",
        "Rest is not a reward you must earn by becoming extraordinary. Even a god knows when to pause.",
    ],

    "pure_nonsense": [
        "The sun is shining. Naturally. You're welcome.",
        "You summoned me just to read this? I shall remember.",
        "Hermes says you have too many tabs open. He would know.",
        "I have heard things about your screen time.",
        "The moon is doing wonderfully. Thank you for asking.",
        "You could say thank you, you know. I am choosing to be magnanimous.",
        "I was contemplating eternity. But very well.",
        "Few mortals have the privilege of being judged by me. Do try to savour it.",
        "Everything revolves around something. In my case, quite literally.",
        "Go on, then. Make me proud. Or at least entertain me.",
        "Someone may think of you today. Whether they reply to your message remains beyond my jurisdiction.",
    ],
}


# ---------- Public functions ----------

def get_random_commentary():
    """Return a randomly selected commentary message."""
    category = random.choices(
        population=list(CATEGORY_WEIGHTS.keys()),
        weights=list(CATEGORY_WEIGHTS.values()),
        k=1,
    )[0]

    return random.choice(COMMENTARY[category])
