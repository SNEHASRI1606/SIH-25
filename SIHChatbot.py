import openai

# Your Groq API Key
openai.api_key = "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"

# Use Groq's custom API base
openai.api_base = "https://api.groq.com/openai/v1"

MODEL = "llama3-70b-8192"


def chat():
    print(" Hello! How may I help you today!!!")
    print("💬 Start chatting! Type 'exit' to stop.")
    print("📝 This chatbot specializes in SCD-V Division scholarship schemes and Aadhaar seeding information")

    # Enhanced system prompt to strictly control the topic
    system_prompt = """You are a specialized assistant for SCD-V Division, DoSJE scholarship schemes. 
    Your expertise is limited to:
    - Pre-Matric and Post-Matric scholarship schemes for SC students
    - Direct Beneficiary Transfer (DBT) enabled Aadhaar seeded bank accounts
    - Difference between Aadhaar linked vs DBT-enabled Aadhaar seeded accounts
    - Scholarship disbursement procedures
    - Aadhaar seeding awareness programs through Gram Panchayats, school committees, and parent-teacher meetings

    If asked about any other topic, politely decline and redirect the conversation back to scholarship schemes 
    and Aadhaar seeding procedures. Do not provide information on any other subjects."""

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