import openai
import os
from getpass import getpass

# Your Groq API Key - try to get from environment first
openai.api_key = os.environ.get("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") 

# If the hardcoded key doesn't work, prompt user
try:
    # Test if the key works with a simple validation
    openai.ChatCompletion.create(
        model="llama3-70b-8192",
        messages=[{"role": "system", "content": "test"}],
        max_tokens=5
    )
except:
    print("🔐 API key not working. Please enter your Groq API key.")
    print("You can get it from: https://console.groq.com/keys")
    openai.api_key = getpass("Enter your API key: ")

# Use Groq's custom API base
openai.api_base = "https://api.groq.com/openai/v1"

MODEL = "llama3-70b-8192"

def chat():
    print(" Welcome to your Groq-powered chatbot!")
    print("💬 Start chatting! Type 'exit' to stop.")

    # Initialize chat history
    messages = [{"role": "system", "content": "You are a helpful assistant that only discusses SCD-V Division scholarship schemes, Aadhaar seeding procedures, and related topics. If asked about other subjects, politely decline and redirect to the specified topics."}]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            break

        # Add user's message
        messages.append({"role": "user", "content": user_input})

        try:
            # Call Groq API
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=messages
            )

            # Get and print assistant reply
            reply = response["choices"][0]["message"]["content"]
            print("🤖 Bot:", reply)

            # Save assistant reply to history
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("❌ Error:", e)
            # If it's an authentication error, prompt for new key
            if "authentication" in str(e).lower() or "401" in str(e):
                print("🔐 Authentication failed. Please enter a valid API key.")
                openai.api_key = getpass("Enter your API key: ")

# Run the chatbot
if __name__ == "__main__":
    chat()
