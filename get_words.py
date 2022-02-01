import requests

# This code gets random words from the api and returns them together as a list.
paramaters = {
    "count" : 100,
}

url = "https://random-word-form.herokuapp.com/random/"

class Text:
    def __init__(self):
        self.nouns = requests.get(f'{url}noun', params=paramaters)
        self.nouns = self.nouns.json()

        self.adjectives = requests.get(f'{url}adjective', params=paramaters)
        self.adjectives = self.adjectives.json()

        self.animals = requests.get(f'{url}animal', params=paramaters)
        self.animals = self.animals.json()

        self.text = []

    def form_text(self):
        for i in range(100):
            self.text.extend([self.nouns[i], self.adjectives[i], self.animals[i]])

        # self.text = " ".join(self.text)

        return self.text

if __name__ == '__main__':
    paragraph = Text()
    print(paragraph.form_text())