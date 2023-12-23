from openai import OpenAI
import os
from dotenv import load_dotenv
import time
import json


class OpenAIOperator:
    def __init__(self, api_key, model="gpt-4-1106-preview"):
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.tools = [{"type": "retrieval"}]

    def create_assistant(self, name, instructions):
        self.assistant = self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            model=self.model,
            tools=self.tools
        )

    def start_thread(self):
        self.thread = self.client.beta.threads.create()

    def create_message(self, content):
        self.message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content
        )

    def execute_run(self):
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
        )
        return self.wait_on_run(run)

    def wait_on_run(self, run):
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run

    def show_json(self, obj):
        print(json.dumps(json.loads(obj.model_dump_json()), indent=4))

    def list_messages(self):
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        self.show_json(messages)

# Example usage:
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
operator = OpenAIOperator(api_key)

operator.create_assistant(
    name="Data visualizer",
    instructions="Take a deep breath and go step by step with your answers. You are a medical professional and "
                 "researcher in the field of medicine, nutrition, exercise and statistics."
)

operator.start_thread()
operator.create_message("Talk about Ivermectin")
run = operator.execute_run()
operator.show_json(run)
operator.list_messages()
