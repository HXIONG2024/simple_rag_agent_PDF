# RAG Agent for PDF Documents

A Retrieval-Augmented Generation (RAG) system that leverages Google's Gemini model to provide intelligent responses to queries about PDF documents.

## Features

- **LLM Integration**: Utilizes Google's Gemini model for natural language understanding and response generation
- **Embedding**: Implements OpenAI's Text-embedding-ada-002 model for document embedding
- **Vector Store**: Uses FAISS (Facebook AI Similarity Search) for efficient local vector storage and retrieval
- **Framework**: Built with pydantic-ai for robust agent development and quality control
- **Document Support**: Successfully tested with large PDF documents (500+ pages, ~9MB)

## Technical Insights

### Vector Store Implementation
- FAISS was chosen for its exceptional performance in similarity search operations
- The system utilizes Euclidean Distance for similarity measurements (lower distance indicates higher similarity)

### Best Practices
- **Prompt Engineering**: Careful attention to prompt design, especially within tools
- **Tool Development**: Include example inputs in tool specifications for improved agent comprehension
- **Quality Control**: Leverages pydantic-ai's built-in validation and type checking

## Project Status

This project serves as a learning implementation of RAG systems. While functional, it's primarily intended for educational purposes and demonstration of RAG concepts.

## Contributing

Feedback and suggestions are welcome! If you have ideas for improvements or spot areas that could be enhanced, please feel free to contribute.

## Disclaimer

This is a learning-focused project. While efforts have been made to ensure quality, it may not be suitable for production environments without further refinement.
