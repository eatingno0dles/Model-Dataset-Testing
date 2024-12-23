from openai import OpenAI
client = OpenAI()
batch_status = client.batches.retrieve('batch_67561e58df3c819196e852b90483c4ee')
print(batch_status.status)
if batch_status.status == "completed":
    output_file = client.files.retrieve(batch_status.output_file_id)
    with open("batchResults.jsonl", "wb") as file:
        contents = client.files.content(output_file.id).content
        file.write(contents)
    print("Batch results retrieved and saved to batchResults.jsonl")
    