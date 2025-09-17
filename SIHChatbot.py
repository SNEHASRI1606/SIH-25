import openai


openai.api_key = "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"

# Use Groq's custom API base
openai.api_base = "https://api.groq.com/openai/v1"

# Updated model - using the latest Llama 3.1 model
MODEL = "llama-3.1-70b-versatile"


def chat():
    print(" Welcome to your Groq-powered chatbot!")
    print("💬 Start chatting! Type 'exit' to stop.")

    # Updated system prompt to focus only on the specified topic
    system_prompt = """You are a specialized assistant for SCD-V Division, DoSJE scholarship schemes. 
    Your expertise is limited to:
    - Pre-Matric and Post-Matric scholarship schemes for SC students
    - Direct Beneficiary Transfer (DBT) enabled Aadhaar seeded bank accounts
    - Difference between Aadhaar linked vs DBT-enabled Aadhaar seeded accounts
    - Scholarship disbursement procedures
    - Aadhaar seeding awareness programs

    If asked about any other topic, politely decline and redirect the conversation back to scholarship schemes 
    and Aadhaar seeding procedures. Do not provide information on any other subjects."""

    # Initialize chat history with the focused system prompt
    messages = [{"role": "system", "content": system_prompt}]

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


# Run the chatbot
if __name__ == "__main__":
    chat()

