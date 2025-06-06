# gRPC Sentiment Analysis

This project implements a gRPC service for sentiment analysis using the TextBlob library. It allows clients to send text data to a server and receive sentiment analysis results.

## Project Structure

```
grpc-sentiment-analysis
├── src
│   ├── server.py                # Entry point for the gRPC server
│   ├── client.py                # Client implementation for communicating with the server
│   ├── sentiment_analysis.proto  # gRPC service definition and message types
│   └── utils
│       └── textblob_helper.py   # Helper functions for sentiment analysis using TextBlob
├── Dockerfile                    # Instructions for building the Docker image
├── requirements.txt              # Python dependencies for the project
└── README.md                     # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd grpc-sentiment-analysis
   ```

2. **Install dependencies:**
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Run the gRPC server:**
   Execute the following command to start the server:
   ```
   python src/server.py
   ```

4. **Run the client:**
   In a separate terminal, run the client to send text for sentiment analysis:
   ```
   python src/client.py
   ```

## Usage Example

After starting the server, you can use the client to send a text string. The client will display the sentiment polarity and subjectivity returned by the server.

## Docker

To build and run the application in a Docker container, use the following commands:

1. **Build the Docker image:**
   ```
   docker build -t grpc-sentiment-analysis .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 50051:50051 grpc-sentiment-analysis
   ```

## License

This project is licensed under the MIT License.