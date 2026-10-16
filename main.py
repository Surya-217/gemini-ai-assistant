
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"

def create_chat(client):
    return client.chats.create(
        model=MODEL,
        config={
            "system_instruction": (
                "You are a concise personal AI assistant. "
                "Answer in 3 sentences maximum by default. "
                "Use simple English. "
                "Do not add headings, bullet points, examples, or summaries "
                "unless the user explicitly requests them. "
                "Follow the user's requested response length."
            )
        }
    )

def main():
    
    client = genai.Client(
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(
                attempts=5,
                initial_delay=1.0,
                exp_base=2.0,
                max_delay=10.0,
                http_status_codes=[408, 429, 500, 502, 503, 504],
            )
        )
    )


    chat = create_chat(client)

    print("AI Assistant ready! Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() in ("exit", "/exit"):
            print("Assistant: Goodbye!")
            break

        if prompt.lower() == "/clear":
            chat = create_chat(client)
            print("Assistant: Conversation cleared!\n")
            continue

        if prompt.lower() == "/help":
            print("\nAvailable commands:")
            print("  /help  - Show available commands")
            print("  /clear - Start a fresh conversation")
            print("  /exit  - Quit the assistant\n")
            continue
        
        if not prompt:
            print("Please enter a message.")
            continue

        try:
            response = chat.send_message(prompt)
            print("\nAI:", response.text, "\n")

        except Exception as error:
            message = str(error).lower()

            if any(term in message for term in (
                "getaddrinfo failed",
                "connection error",
                "network is unreachable",
                "timed out",
            )):
                print("Network error: Check your internet connection and try again.")
            else:
                print("Request failed:", error)



if __name__ == "__main__":
    main()
