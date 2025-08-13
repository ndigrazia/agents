import os
import asyncio
from openai import AsyncOpenAI

async def main():
    # Read API key from environment variable
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set.")

    # Create async client for Perplexity API
    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.perplexity.ai"
    )

    # Send async chat completion request
    response = await client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "user", "content": "What's the capital of France?"}
        ]
    )

    # Print the assistant's reply
    print(response.choices[0].message.content)

# Run async main
if __name__ == "__main__":
    asyncio.run(main())