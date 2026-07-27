from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("==== My First AI Agent ====")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI Agent: Goodbye!")
        break

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )

        print("\nAI:", response.output_text)
        print("-" * 50)

    except Exception as e:
        print("Error:", e)