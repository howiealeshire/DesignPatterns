'''
Taken from: https://realpython.com/python-microservices-grpc/#example-implementation

"In order to simplify the workflow with big applications, we can split it into smaller parts.
Each part serves one particular purpose. We call that a "(web) service".
These web services are very flexible to use.
You can use them from within your existing monolithic application, either in the server part, or in the client part.
You can also have web services that use other web services.

The split into single web services allows you to loosely couple your application.
This means that as a user of the service you only depend on the service being up, available and working.
You no longer need to take care of its dependencies, its compilation, deployment or testing.
(There are even ways of decoupling further through events on queues, or on a bus.)
" - https://stackoverflow.com/questions/46575898/what-is-a-microservice

Frequently, a microservice serves one purpose, contains its own data (usually in the form of its own db), and has
an exposed API that operates on specific protocols (usually HTTP) that allows for exchange of data between the calling
client, the microservices, and even communication between microservices. The most common data transfer format between
these are either JSON or XML.

This microservice goes a different route however, and implements the microservice over Remote Procedure Call (RPC).
This goes into detail as to why you might want to implement (a) microservice(s) this way:
https://realpython.com/python-microservices-grpc/#why-rpc-and-protocol-buffers



'''

from concurrent import futures
import random
import grpc
from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)

import recommendations_pb2_grpc

# this is the db of the microservice, implemented as a dictionary. Obviously, in a real application, we'd use a
# production grade db, e.g. Postgres.
books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(
            id=4, title="The Hitchhiker's Guide to the Galaxy"
        ),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"\
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
}

class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    # The API
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )
        return RecommendationResponse(recommendations=books_to_recommend)

def serve():
    # This microservice also implements the way to serve itself.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":

    serve()