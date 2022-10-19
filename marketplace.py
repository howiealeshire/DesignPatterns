syntax = "proto3";


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