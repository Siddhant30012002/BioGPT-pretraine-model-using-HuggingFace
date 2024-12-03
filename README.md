# BioGPT-based Drug Information Generator using Transformer

This project uses Microsoft’s pre-trained BioGPT model, available on Hugging Face based on Transformer which is mainly known for the **attention mechanism** to provide information about drugs. The model generates text about a given drug's use case by using a natural language processing (NLP) approach. The application is built using Streamlit, where users can input the name of a drug to get its usage details.

## Features
- Text generation for drug usage information.
- Interactive form to input drug names.
- Uses BioGPT pre-trained model for context-based responses.
- Provides real-time responses through Streamlit.

## Technologies
- **Python**: The core programming language for this project.
- **Streamlit**: Used for creating the interactive web interface.
- **Hugging Face's Transformers**: For leveraging BioGPT's pre-trained model.

## How It Works
- The user inputs a drug name in the form.
- BioGPT model generates a description of the drug's usage.
- The response is displayed in the Streamlit interface.

## Model Details
- **Model**: microsoft/biogpt from Hugging Face.
- **Tokenizer**: BioGptTokenizer is used for tokenizing the drug name input.
- **Pipeline**: The Hugging Face pipeline for text generation is utilized.

## Development Insights
**After many trials with different prompting techniques, including zero-shot, one-shot, and few-shot prompting, I encountered issues with getting accurate responses. This was due to the limited trainable parameters in BioGPT. After several iterations, I found that a simple prompt template, such as "the {drug_name} is used in condition of", generated the most reliable responses.**

## Future Enhancements
- Expand to handle more specific drug-related queries.
- Improve the user interface for better interaction.
