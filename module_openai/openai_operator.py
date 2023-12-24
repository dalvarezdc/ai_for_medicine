from openai import OpenAI
import os
from dotenv import load_dotenv
import time
import json
from typing import Any, Dict
from prompts.generic_prompts import MEDICINE_INSTRUCTIONS

class OpenAIOperator:
    """Class to operate OpenAI's API for creating assistants, threads, and executing runs."""

    def __init__(self, api_key: str, model: str = "gpt-4-1106-preview") -> None:
        """Initializes the OpenAIOperator with API key and model configuration.

        Args:
            api_key (str): API key for authenticating with the OpenAI service.
            model (str): Model name to be used with OpenAI. Default is "gpt-4-1106-preview".
        """
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.tools = [{"type": "retrieval"}]

    def create_assistant(self, name: str, instructions: str) -> None:
        """Creates an assistant with the given name and instructions.

        Args:
            name (str): Name for the assistant.
            instructions (str): Instructions or description for the assistant.
        """
        self.assistant = self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            model=self.model,
            tools=self.tools
        )

    def start_thread(self) -> None:
        """Starts a new thread for communication with the assistant."""
        self.thread = self.client.beta.threads.create()

    def create_message(self, content: str) -> None:
        """Creates a message in the current thread.

        Args:
            content (str): The content of the message to be sent.
        """
        self.message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content
        )

    def execute_run(self) -> Any:
        """Executes a run using the current assistant and thread, and waits for the run to complete.

        Returns:
            Any: The result of the run.
        """
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
        )
        return self.wait_on_run(run)

    def wait_on_run(self, run: Any) -> Any:
        """Waits for the provided run to complete.

        Args:
            run (Any): The run object to wait on.

        Returns:
            Any: The completed run object.
        """
        while run.status == "queued" or run.status == "in_progress":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run

    def show_json(self, obj: Any) -> None:
        """Prints the JSON representation of the given object.

        Args:
            obj (Any): The object to be converted to JSON and printed.
        """
        print(json.dumps(json.loads(obj.model_dump_json()), indent=4))

    def list_messages(self) -> None:
        """Lists all messages in the current thread."""
        messages = self.client.beta.threads.messages.list(thread_id=self.thread.id)
        self.show_json(messages)


