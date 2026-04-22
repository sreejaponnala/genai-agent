from utils import get_pricing_info, validate_email

def mock_lead_capture(name, email, platform):
    print(f"\nLead captured successfully: {name}, {email}, {platform}\n")

def chat():
    print("Agent: Hi! I can help you with AutoStream 😊")

    while True:
        user = input("You: ").strip().lower()

        if "price" in user or "plan" in user:
            print(get_pricing_info())

        elif "refund" in user or "policy" in user:
            print("Agent: We offer a 7-day refund policy.")
            print("Agent: No refunds after that.")
            print("Agent: 24/7 support is available only on Pro plan.")

        elif user in ["hi", "hello", "hey"]:
            print("Agent: Hello! Ask me about pricing or plans.")

        elif "buy" in user or "try" in user or "interested" in user:
            name = input("Agent: Your name: ")

            email = input("Agent: Your email: ")
            while not validate_email(email):
                print("Agent: Please enter a valid email.")
                email = input("Agent: Your email: ")

            platform = input("Agent: Platform (YouTube/Instagram): ")

            mock_lead_capture(name, email, platform)
            print("Agent: Done! Our team will contact you soon.")
            break

        else:
            print("Agent: I can help with pricing or plans.")

if __name__ == "__main__":
    chat()