import spacy

class FOPCParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def parse_fopc(self, expression):
        doc = self.nlp(expression)
        return self._parse(doc)

    def _parse(self, doc):
        parsed_tokens = []

        for token in doc:
            if token.dep_ in ['nsubj', 'attr', 'dobj', 'prep']:
                parsed_tokens.append(token.text)

        return " ".join(parsed_tokens)

if __name__ == "__main__":
    fopc_parser = FOPCParser()

    # Example usage:
    expression = "Cats are mammals with fur"
    parsed_expression = fopc_parser.parse_fopc(expression)
    print(f"Input expression: {expression}")
    print(f"Parsed FOPC expression: {parsed_expression}")
    
