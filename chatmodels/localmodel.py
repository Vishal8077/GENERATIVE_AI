from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama_v1.1", 
    task="text-generation",
    model_kwargs={"temperature": 0.7, "max_new_tokens":512, "top_k": 50, "repetition_penalty": 1.03},
)

chat_model = ChatHuggingFace(llm=llm_pipeline)

result = chat_model.invoke("what is cricket?")

print(result.content)