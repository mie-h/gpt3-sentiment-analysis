import openai
from decouple import config
import argparse

openai.api_key=config('OPENAI_API_KEY')

def generate_prompt(text):
    return """This is a Sentence sentiment classifier

        Sentence: I loved the new restaurant!
        Sentiment: Positive
        ###
        Sentence: This sucks. I'm bored.
        Sentiment: Negative
        ###
        Sentence: I don't like how this is going.
        Sentiment: Negative
        ###
        Sentence: {}
        Sentiment:""".format(text)

def process_output(resp):
    output_txt = resp['choices'][0]['text']
    sentiment = output_txt.split('\n')[0]
    return sentiment

def sentiment_analysis(text):
    print(f"The given text is: { text }")

    prompt = generate_prompt(text)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.6,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["###"])

    
    sentiment = process_output(response)
    print(f"Sentiment: { sentiment }")


def main():
    parser = argparse.ArgumentParser(description='Process sentiment analysis.')
    parser.add_argument('--text')
    args = parser.parse_args()
    sentiment_analysis(args.text)

if __name__ == "__main__":
    main()