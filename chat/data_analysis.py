import spacy

class text_mining:

    def __init__(self, text):
        self.text = text

    def identify_name(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        temp = '-1'
        
        for token in doc:
            if(token.pos_ == 'PROPN' ):
                return(token.text)

            if(token.pos_ == 'NOUN'):
                temp = token.text
        
        if(temp != '-1'):
            return temp
        return('0')