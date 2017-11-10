def create_pipeline(es, params):
    s = es.ingest.put_pipeline(id=params["pipeline-definition"]["name"], body=params["pipeline-definition"]["body"])
    return 1, "ops"

def register(registry):
    registry.register_runner("create-pipeline", create_pipeline)
