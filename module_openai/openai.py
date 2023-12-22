from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
  name="Data visualizer",
  description="Take a deep breath and go step by step with your answers. You are a medical professional and "
              "researcher in the field of medicine, nutrition, exercise and statistics.",
  model="gpt-4-1106-preview",
  tools=[{"type": "code_interpreter"}],
  # file_ids=[file.id]
)