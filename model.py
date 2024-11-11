from openai import OpenAI
import os

client= OpenAI(
    api_key= 'OPENAI_API_KEY',
)

response = client.files.create(
    file=open("modelTraining.jsonl", "rb"),
    purpose="fine-tune"
)

client.fine_tuning.jobs.create(
    training_file=response.id,
    model="gpt-4o-mini-2024-07-18",
)