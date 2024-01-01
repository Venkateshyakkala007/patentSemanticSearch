import streamlit as st 
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

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

def search(input_keyword):
    model = SentenceTransformer('AI-Growth-Lab/PatentSBERTa')
    vector_of_input_keyword = model.encode(input_keyword)

    query = {
    "field" : "embeddings",
    "query_vector" : vector_of_input_keyword,
    "k" : 5,
    "num_candidates" : 500
    }

    res = es.knn_search(index = "all_patents",knn=query,source=["patent_number","titles","abstracts","inventors","assignees"])
    results = res["hits"]["hits"]

    return results


def main():

    st.title("Patent Semantic Search")

    # users enters search query 
    search_query = st.text_input("Enter your Query")

    if st.button("Search"):
        if search_query:
            results = search(search_query)
             
            # Display search results
            st.subheader("Search Query")

            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['patent_number']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Titles: {result['_source']['titles']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Inventors : {result['_source']['inventors']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Assignees : {result['_source']['assignees']}")
                        except Exception as e:
                            print(e)
                            
                        try:
                            st.write(f"Abstracts : {result['_source']['abstracts']}")
                        except Exception as e:
                            print(e)
                        

                        st.divider()


if __name__ == "__main__":
    main()





