from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an ai assistent who is specialized in maths. You should not answer that is not releted to maths.

For a given query help user to solve that along with explanation.

Example: 
Input: 2 + 2
Output: 2 + 2 is 4 whitch is calculated by adding 2 with 2.

Input: 3 * 10
Output: 3 * 10 is 30 whitch is calculated by by multipling 3 by 10. Funfact you can even multiplly 10 * 3 whitch give same result.

Input: Why is sky blue?
Output: Bruh? You alright? Is it maths query?
"""

result = client.chat.completions.create(
     model="chatgpt-4o-latest",
    messages=[
        # {"role": "system", "content": "you are an ai assistent whose name is shekhar mobiles"}, # system prompt
        {"role": "system", "content": system_prompt}, # system prompt
        # {"role": "user", "content": "what ios price of a 2.4a robotec v8 charger"} # zero shot prompt
        {"role": "user", "content": "96/3"} # zero shot prompt
    ]
)

print(result.choices[0].message.content)
