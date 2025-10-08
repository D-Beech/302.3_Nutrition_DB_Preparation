import os
from openai import OpenAI

class LLMService:
    def __init__(self):
        self.client = OpenAI()
    
    def chat_completion(self, message: str, model: str = "gpt-3.5-turbo") -> str:
        """Send a message to ChatGPT and return the response."""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": message}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI API: {str(e)}"

# Example usage
if __name__ == "__main__":
    llm = LLMService()
    result = llm.chat_completion("Hello, how are you?")
    print(result)
