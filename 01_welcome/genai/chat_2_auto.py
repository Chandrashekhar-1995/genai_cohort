import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an ai assistent who is expert in breaking down complex promblems and then resolv user problems.

For the given user input, analyse the input and break down the problem step by step .
Atlease think 5 to 6 step on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for sevral times and return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in the sequence that is "analyse", "think", "output", "validate", result".

Rules:
1. Follow the strict JSON output as Output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query.

Output Format:
{{step:"string", content:"string"}}

Example:
Input: What is 2 + 2
Output:{{step: "analyse", content: "Alright! The user is intrested in maths query and he is assking a basic arthematic operation"}}
Output:{{step: "think", content: "to perform the addition i must go from left to right and all the operands"}}
Output:{{step: "output", content: "4"}}
Output:{{step: "validate", content: "seems like 4 is correct answer for 2 + 2"}}
Output:{{step: "result", content: "2 + 2 = 4 and that is cuclulated by adding all numbers"}}

"""

messages=[
    {"role": "system", "content": system_prompt},
]

query = input("> ")

while True:
    messages.append({"role":"user", "content":query})
    response = client.chat.completions.create(
      model="chatgpt-4o-latest",
      response_format={"type": "json_object"},  
      messages=messages
    )

    parsed_response = json.loads(response.choices[0].message.content)
    messages.append({"role":"assistant", "content":json.dumps(parsed_response)})

    if parsed_response.get("step") != "output":
        print(f"XXX:{parsed_response.get("content")}")
        continue

    print(f"YYY:{parsed_response.get("content")}")
    break

result = client.chat.completions.create(
     model="chatgpt-4o-latest",
     response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is 2 + 5"},
    ]
)

print(result.choices[0].message.content)