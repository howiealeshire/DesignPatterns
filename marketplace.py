syntax = "proto3";
/* these are the data structures and the outline for the API responses returned by the microservice. gRPC library takes these and generates the API 
"Python is a little different — the Python compiler generates a module with a static descriptor of each message type in your .proto, 
which is then used with a metaclass to create the necessary Python data access class at runtime." - https://developers.google.com/protocol-buffers/docs/proto3

*/

enum BookCategory {

    MYSTERY = 0;

    SCIENCE_FICTION = 1;

    SELF_HELP = 2;

}


message RecommendationRequest {

    int32 user_id = 1;

    BookCategory category = 2;

    int32 max_results = 3;

}


message BookRecommendation {

    int32 id = 1;

    string title = 2;

}


message RecommendationResponse {

    repeated BookRecommendation recommendations = 1;

}


service Recommendations {

    rpc Recommend (RecommendationRequest) returns (RecommendationResponse);

}
