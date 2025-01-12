import urequests
import ujson

class OpenAI:
    def __init__(self, api_key, model="", url=""):
        self.api_key = api_key
        self.model = model
        self.url = url
        self.chat_history = []

    def chat(self, message, mode="continue"):
        pass

class DeepSeek:
    def __init__(self, api_key, model="deepseek-chat", url="https://api.deepseek.com/chat/completions"):
        self.api_key = api_key
        self.model = model
        self.url = url
        self.chat_history = []
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def chat(self, message, mode="continue"):
        if mode == "new":
            self.chat_history = []
            self.chat_history.append({"role": "system", "content": "You are a helpful assistant"})
            self.chat_history.append({"role": "system", "content": "Don't give me emoji."})

        self.chat_history.append({"role": "user", "content": message})

        payload = {
            "model": self.model,
            "messages": self.chat_history,
            "stream": False
        }
        

        response = urequests.post(self.url, data=ujson.dumps(payload), headers=self.headers)

        if response.status_code == 200:
            self.chat_history.append(ujson.loads(response.text)['choices'][0]['message'])
            return self.chat_history[-1]["content"]
        else:
            self.chat_history.pop()
            print('Fail, retry manually.')




  

