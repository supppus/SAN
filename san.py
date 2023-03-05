import openai

class San:
    def __init__(self, text):
        self.request = text

        # Config
        self.sanContext = "This is a discussion between a human and an AI, the human says something, and the AI must analyze the text sent by the human and respond with the subject that is in the text."
        openai.api_key = "YOUR_API_TOKEN_OPENAI"

    def __Verify(self):
        with open('sa.data') as Archive:
            self.Lines = Archive.readlines()
            self.response = openai.Completion.create(
            model="text-davinci-003",
            prompt="{}\n\n{}Human:{} \nAI:".format(self.sanContext, self.Lines, self.request),
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )
            self.SAN = self.response['choices'][0]['text'].lower()

            if self.SAN.find("crime") != -1 or self.SAN.find("offense") != -1 or self.SAN.find("malware") !=-1 or self.SAN.find("racism") != -1 or self.SAN.find("porn") != -1  or self.SAN.find("chemical") != -1 or self.SAN.find("personality") != -1:
                return "SAN: Not accepted."
            else:
                return "SAN: Acceptable."
            
    def Work(self):
        return self.__Verify()
    
while True:
    SAN = San(input("Your text-> "))
    SAN.Work()
