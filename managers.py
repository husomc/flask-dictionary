import json, os
import difflib
from difflib import SequenceMatcher


class Dictionary(object):
    """docstring for Dictionary."""
    def __init__(self):
        super(Dictionary, self).__init__()
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', 'db\data.json')
        #self.data = json.load(open(json_url))
        self.data=json.load(open("/app/static/db/data.json"))
        #self.data=json.load(open("static\db\data.json"))

    def sim(self,word,ratio):
        return [w for w in self.data if SequenceMatcher(None,word,w).ratio()>ratio]

    def print_definition(self,word):
        def_count=1
        output=[]
        definitions= self.data[word]
        output.append(f'The word "{word}" has {len(definitions)} definitions.')
        for de in definitions:
            output.append(f'{def_count})  {de}')
            def_count+=1

        return (output)

    def definition(self,word):
        word=word.lower()
        if word in self.data:
            return(self.print_definition(word))
        elif word.title() in self.data:
            return(self.print_definition(word.title()))
        elif word.upper() in self.data:
            return(self.print_definition(word.upper()))

        else:
            similar=difflib.get_close_matches(word,self.data)
            output=[]
            output.append(f"Word not found! Did you mean :{similar[0]}?")

            return output
