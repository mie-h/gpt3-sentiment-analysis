import openai


openai.api_key=''




def generate_prompt(text):
    return """This is a Sentence sentiment classifier

        Sentence: I loved the new Batman movie!
        Sentiment: Positive
        ###
        Sentence: I hate it when my phone battery dies.
        Sentiment: Negative
        ###
        Sentence: I don't like this.
        Sentiment: Negative
        ###
        Sentence: {}
        Sentiment:""".format(text)



prompt = generate_prompt("Hello I am not feeling well today.")
print(prompt)

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.6,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["###"])
print (response)
