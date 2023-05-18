import openai

openai.api_key = "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"

def get_GPTanswer(Question):
    Question = f"Answer that: {Question} "
    response = openai.Completion.create(
        engine="davinci",
        prompt=Question,
        max_tokens=400,
        n=1,
        stop="\n",  # Set a stop sequence here
        temperature=0.7,
    )
    return response.choices[0].text.strip()