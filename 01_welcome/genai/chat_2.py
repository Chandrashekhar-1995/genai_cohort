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

result = client.chat.completions.create(
     model="chatgpt-4o-latest",
     response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is 3 + 4 * 5"},
        #
        {"role": "assistant", "content": json.dumps({ "step": "analyse", "content": "The user has entered a mathematical expression involving both addition and multiplication. Understanding the order of operations (PEMDAS/BODMAS) is critical here." })},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "According to the order of operations, multiplication takes precedence over addition. So, in 3 + 4 * 5, the multiplication (4 * 5) should be calculated first."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "Now, computing 4 * 5 gives 20. After that, we add 3 to the result: 3 + 20."})},
    ]
)

print(result.choices[0].message.content)