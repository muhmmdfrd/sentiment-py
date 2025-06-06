from concurrent import futures
import grpc
import sentiment_analysis_pb2
import sentiment_analysis_pb2_grpc
from utils.textblob_helper import analyze_sentiment

VALID_API_KEY = "yyWq@TAN2j#@j@SCKDjTVqdZxW6N60zJJ4^v2#Y6d7b6C3y!f#0Xx5YBV!NT&mZt"

class SentimentAnalysisService(sentiment_analysis_pb2_grpc.SentimentAnalysisServicer):
    def AnalyzeSentiment(self, request, context):
        # Extract API key from metadata
        api_key = dict(context.invocation_metadata()).get("api-key")
        
        # Validate API key
        if api_key != VALID_API_KEY:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid or missing API key.")
            return sentiment_analysis_pb2.SentimentResponse()
        
        # Perform sentiment analysis
        text = request.text
        sentiment, subjectivity = analyze_sentiment(text)
        return sentiment_analysis_pb2.SentimentResponse(sentiment=sentiment, subjectivity=subjectivity)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentiment_analysis_pb2_grpc.add_SentimentAnalysisServicer_to_server(SentimentAnalysisService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()