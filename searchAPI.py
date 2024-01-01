from flask import Flask,request,jsonify
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

indexName = "all_patents"

try:
    es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic","PQj3k1ehmAhh-3wJ2zyl"),
    ca_certs="elasticsearch-8.11.3/config/certs/http_ca.crt"
    )
except ConnectionError as e:
    print("Connection Error" , e)


if es.ping():
    print("Successfully connected to ElasticSearch!")
else:
    print("Oops!! Can not conencted to Elastic Search!")




@app.route("/search/<query>")
def get_data(query):

    model = SentenceTransformer('AI-Growth-Lab/PatentSBERTa')
    vector_of_input_keyword = model.encode(query)

    ans = {
    "field" : "embeddings",
    "query_vector" : vector_of_input_keyword,
    "k" : 5,
    "num_candidates" : 500
    }

    res = es.knn_search(index = "all_patents",knn=ans,source=["patent_number","titles","abstracts","inventors","assignees"])
    results = res["hits"]["hits"]

    return jsonify(results),200


if __name__ == '__main__':
    app.run(debug=True)