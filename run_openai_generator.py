import argparse
import os
import asyncio
from dotenv import load_dotenv

from module_openai.openai_async_operator import AsyncOpenAIOperator
from module_openai.openai_operator import OpenAIOperator
from prompts.generic_prompts import MEDICINE_INSTRUCTIONS


async def main():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    operator = AsyncOpenAIOperator(api_key)

    await operator.create_assistant(
        name="Med Book Builder",
        instructions=MEDICINE_INSTRUCTIONS
    )

    await operator.start_thread()
    await operator.create_messages(["Talk about Pizza", "Discuss the benefits of exercise", "Explain machine learning"])
    runs = await operator.execute_run()
    for run in runs:
        operator.show_json(run)
    await operator.list_messages()

def run_synchronous():
    # Example usage:
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    operator = OpenAIOperator(api_key)

    operator.create_assistant(
        name="Data visualizer",
        instructions=MEDICINE_INSTRUCTIONS
    )

    operator.start_thread()
    operator.create_message("Talk about Pizza")
    run = operator.execute_run()
    operator.show_json(run)
    operator.list_messages()


import argparse

parser = argparse.ArgumentParser(description="Example Argparse Program")

# Add arguments
parser.add_argument("run_async", type=bool, default=True, help="will the code run asynchronously")

args = parser.parse_args()

run_async = args.run_async
print(f"run_async: {args.run_async}")

if run_async:
    asyncio.run(main())

elif not run_async:
    run_synchronous()
