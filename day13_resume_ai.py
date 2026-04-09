from openai import OpenAI

client = OpenAI()

print("AI Resume Analyzer started (type 'exit' to quit)")

while True:
    resume  = input("paste your resume text: ")
    
    if resume.lower() == "exit":
        print("AI: Bye")
        break

    response = client.chat.completions.create(
        model = "gpt-40-mini",
        messages=[
            {"role": "system", "content": "you are an expert resume analyzer. Analyze resume and give skills, weakneses, and improvement suggestions."},
            {"role": "user",
             "content": resume}
        ]
    )

    print("\nAI Analysis:\n")

    print(response.choices[0].message.content)

    