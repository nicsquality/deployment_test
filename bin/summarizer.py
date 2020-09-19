import yaml

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config = yaml.load(fl)
        
    def loadDocs(self,filePath):
        with open(filePath,'r') as fl:
            text = fl.read()
        return text
    
    def splitSentences(self,text):
        """
        Split paragraph into an array of sentences
        
        Input:
            text: string
        Output:
            sentences: a list of string
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent