import openai

# Function to generate response using OpenAI's GPT-3.5-turbo
def generate_response(topic):
    prompt = f"Write a detailed paragraph about {topic} and provide a conclusion."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that provides detailed information on topics."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract the AI's response
    ai_response = response['choices'][0]['message']['content']
    return ai_response

# Main program
if __name__ == "__main__":
    openai.api_key = "YOUR_OPENAI_API_KEY"
    
    # Ask the user to input a topic
    topic = input("Enter a topic: ")
    
    # Generate and print the AI's response
    response = generate_response(topic)
    print("\nAI's Response:\n")
    print(response)

