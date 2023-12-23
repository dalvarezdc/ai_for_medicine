from openai import OpenAI

import os
from dotenv import load_dotenv
import time
import json

def show_json(obj):
    print(json.loads(obj.model_dump_json()))

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=api_key)

assistant = client.beta.assistants.create(
  name="Data visualizer",
  instructions="Take a deep breath and go step by step with your answers. You are a medical professional and "
              "researcher in the field of medicine, nutrition, exercise and statistics.",
  # description="Take a deep breath and go step by step with your answers. You are a medical professional and "
  #             "researcher in the field of medicine, nutrition, exercise and statistics.",
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}],
  # file_ids=[file.id]
)



thread = client.beta.threads.create()

print(thread)
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Talk about Ivermectin",
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)


run = wait_on_run(run, thread)
show_json(run)

messages = client.beta.threads.messages.list(thread_id=thread.id)
show_json(messages)
