# Hack-AI-thon

## This is a Retrieval Augmented Generation based chatbot

### The knowledge document was webscraped from a [website](https://www.moveworks.com/) 

 However a simple script can extend this to any website. 

 There are plans to include a UI element in the frontend to include whatever website a user wishes to have go through.

 Simple changes to the backend can make this very versatile chatbot to even accept knowledge documents from any text source.

 Further plans are to make this chatbot multi-modal.

The LLMs supported  for generation are: 

* [Mistral](https://mistral.ai/) [Link to download the model] (https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_S.gguf)
* [GPT](https://platform.openai.com/docs/models)
* [LLama](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) [Link to download model format] (https://huggingface.co/TheBloke/Llama-2-13B-GGUF/blob/main/llama-2-13b.Q4_K_S.gguf)

The LM used for generating embeddings is [MiniLM-L6](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
