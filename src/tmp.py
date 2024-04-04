"""

Dataset example

[
    {
        "instruction": "Can cats communicate?",
        "context": "Cats need to communicate with each other for bonding, and relating with each other; they need to collaborate, play, and share resources...",
        "response": "Cat vocalizations have been categorized according to a range of characteristics...",
    }
]

"""

def generate_prompt(example: dict[str, str]) -> str:
    """Generates a standardized message to prompt the model"""
    return (
        "You are systems analyst at a large corporation. Describe a story for jira issue based on the title. Use the methodology that your company has adopted to do this.\n\n"
        f"### Project description:\n{example['context']}\n\n"
        f"### Story title:\n{example['instruction']}\n\n"
        f"### Story body:{example['response']}"
    )


