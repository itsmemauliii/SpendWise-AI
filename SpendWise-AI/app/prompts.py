
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(df):
    sample = df[["Date", "Amount", "Category", "Description"]].head(20).to_string()
    prompt = f"""
    You're an AI personal finance coach for Gen Z. Analyze the following expenses and give a fun, helpful, Gen Z-style summary.
    Include: top spending categories, a funny roast if needed, and one savings tip. Here’s the data:

    {sample}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
