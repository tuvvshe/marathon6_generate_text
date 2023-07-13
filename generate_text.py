from transformers import pipeline
model = pipeline("text-generation", model = "gpt2")


sentence = model("HOWDY!!, I am DWANE JOHNSON AKA ROCKKK, HERE I AM",
                 do_sample=True, top_k=50,
                 temperature=0.9, max_lenght=100,
                 num_return_sentences=2)

for i in sentence:
    print(i["generate_text"])
