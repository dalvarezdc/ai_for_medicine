import os
import asyncio
from openai import AsyncOpenAI
import json
from typing import Any, List
from dotenv import load_dotenv
from prompts.generic_prompts import MEDICINE_INSTRUCTIONS


class AsyncOpenAIOperator:
    """Class to operate OpenAI's API for creating assistants, threads, and executing runs asynchronously."""

    def __init__(self, api_key: str, model: str = "gpt-4-1106-preview") -> None:
        """Initializes the AsyncOpenAIOperator with API key and model configuration."""
        self.api_key = api_key
        self.model = model
        self.client = AsyncOpenAI(api_key=self.api_key)
        self.tools = [{"type": "retrieval"}]

    async def create_assistant(self, name: str, instructions: str) -> None:
        """Asynchronously creates an assistant with the given name and instructions."""
        self.assistant = await self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            model=self.model,
            tools=self.tools
        )

    async def start_thread(self) -> None:
        """Starts a new thread for communication with the assistant asynchronously."""
        self.thread = await self.client.beta.threads.create()

    async def create_messages(self, contents: List[str]) -> None:
        """Asynchronously creates multiple messages in the current thread."""
        self.messages = []
        for content in contents:
            message = await self.client.beta.threads.messages.create(
                thread_id=self.thread.id,
                role="user",
                content=content
            )
            self.messages.append(message)

    async def execute_run(self) -> Any:
        """Asynchronously executes a run using the current assistant and thread."""
        runs = []
        for message in self.messages:
            run = await self.client.beta.threads.runs.create(
                thread_id=self.thread.id,
                assistant_id=self.assistant.id,
            )
            run = await self.wait_on_run(run)
            runs.append(run)
        return runs

    async def wait_on_run(self, run: Any) -> Any:
        """Asynchronously waits for the provided run to complete."""
        while run.status == "queued" or run.status == "in_progress":
            run = await self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id,
            )
            await asyncio.sleep(0.5)
        return run

    def show_json(self, obj: Any) -> None:
        """Prints the JSON representation of the given object."""
        print(json.dumps(json.loads(obj.model_dump_json()), indent=4))

    async def list_messages(self) -> None:
        """Asynchronously lists all messages in the current thread."""
        messages = await self.client.beta.threads.messages.list(thread_id=self.thread.id)
        self.show_json(messages)

