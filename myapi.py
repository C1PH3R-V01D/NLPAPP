import requests



class API:
    def __init__(self):
        self.url = "https://api.apilayer.com/sentiment/analysis"

        self.headers ={
            "apikey": "fcwt8BcBtWBd5oKVaXvjhE0mgXZaAfro"
        }


    def sentiment_analysis(self, text):
        """Send text to sentiment analysis API and return the response."""
        if not isinstance(text, str) or not text.strip():  # Ensure valid input
            return {"error": "Invalid input. Text must be a non-empty string."}

        payload = text.encode("utf-8")  # Encode text properly
        try:
            response = requests.request("POST", self.url, headers=self.headers, data = payload)
            response.raise_for_status()  # Raise an error if request fails
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}

    def ner(self,text,entity):
        url = "https://api.apilayer.com/nlp/named_entity?lang={}".format(entity)
        payload =text.encode("utf-8")
        response = requests.request("POST", url, headers=self.headers, data=payload)
        result = response.json()
        return result

    def emotion(self,text):
        url = "https://api.apilayer.com/text_to_emotion"
        payload = text.encode("utf-8")
        response = requests.request("POST", url, headers=self.headers, data=payload)
        result = response.json()
        return result


