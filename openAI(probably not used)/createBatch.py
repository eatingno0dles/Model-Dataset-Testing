from openai import OpenAI
client = OpenAI()

batch_input_file = client.files.create(
  file=open("batchPrompts.jsonl", "rb"),
  purpose="batch"
)

batch_input_file_id = batch_input_file.id

print(client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
))