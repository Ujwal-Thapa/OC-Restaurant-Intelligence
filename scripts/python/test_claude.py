import os
from anthropic import Anthropic

# Read API key from your Mac's environment (safer than hardcoding)
client = Anthropic(api_key=os.environ.get("ANTHOPIC_API_KEY"))

# Send a test prompt to Claude
message = client.messages.create(
    model = "claude-sonnet-4-6",
    max_tokens = 200,
    messages = [
        {
            "role": "user",
            "content": "Classify this restaurant into ONE of these cuisine categories: Italian, Mexican, Chinese, Japanese, Thai, Indian, American, Mediterranean, Korean, Vietnamese, French, Other. The Yelp categories are: 'Asian Fusion, Sushi Bars, Japanese'. Reply with just the category name, nothing else."
        }
    ]
)

# Print the result + cost tracking
print("Claude says:", message.content[0].text)
print("Tokens used:", message.usage.input_tokens, "input,", message.usage.output_tokens, "output")