from elasticsearch import Elasticsearch 

    # Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 8080, 'scheme': 'http'}])

def match_job_description(job_description, resume):
    # Define Elasticsearch query
    query = {
        "query": {
            "match": {
                "content": job_description
            }
        }
    }
    
    # Search for job description in Elasticsearch index
    response = es.search(index="resumes", body=query)
    
    # Return matching resumes
    return [hit["_source"] for hit in response["hits"]["hits"]]

# Example usage
job_description = "Software Engineer with experience in Python and Java"
resume = "Experienced Software Engineer proficient in Python and Java"

matched_resumes = match_job_description(job_description, resume)
print("Matched Resumes:")
for resume in matched_resumes:
    print(resume)

