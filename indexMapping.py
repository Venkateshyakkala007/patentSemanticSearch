indexMapping = {
    "properties" :{
        "patent_number":{
            "type" : "text"
        },
        "publication_id" :{
            "type" : "long"
        },
        "family_id" : {
            "type" : "long"
        },
        "publication_date":{
            "type" : "text"
        },
        "ipc_classes":{
            "type" : "text"
        },
        "legal_status":{
            "type" : "text"
        },
        "priority_date":{
            "type" : "text"
        },
        "application_date":{
            "type" :"text"
        },
        "titles":{
            "type" : "text"
        },
        "abstracts":{
            "type" :"text"
        },
        "description":{
            "type" : "text"
        },
        "inventors":{
            "type" : "text"
        },
        "assignees":{
            "type" : "text"
        },
        "combined":{
            "type" : "text"
        },
        "embeddings":{
            "type" : "dense_vector",
            "dims": 768,
            "index" : True,
            "similarity": "l2_norm"
        },
        "ucid" :{
            "type" : "text"
        }
    }
}