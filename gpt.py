import requests
import json

def predict(input_text):
    import requests
    data = {
        "context": input_text,
        "max_time": 1,
        "model_size": "gpt2/large",
        "temperature": 1,
        "top_p": 1
    }
    data = requests.post('https://transformer.huggingface.co/autocomplete/gpt2/large', json=data)
    return json.loads(data.content)

def get_prediction(input_text):
    pred = predict(input_text)['sentences'][0]['value']
    # print(pred)

    def t(pred):
        for i in ['.',"?", '!']:
            if i in pred:
                return False
        return True
    while t(pred) :
        input_text+=pred
        pred = predict(input_text)['sentences'][0]['value']

    for i in ['.', "?", '!']:
        if i in pred:
            pred = pred.split(i)[0] +i

    return input_text+pred



