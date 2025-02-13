MODEL_ID="ibm-granite/granite-3.1-2b-instruct"
TASK="text-generation"
MODEL_PARAMS={
    "max_new_tokens": 1024,
    "top_k": 50,
    "temperature":0,
    "top_p":200,
    "repetition_penalty":1.1
}