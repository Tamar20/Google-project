
class Trie(object):
    def __init__(self):
        self.child = {}

    def insert(self, word, path, line_num, offset):
        current = self.child
        for l in word:
            if l not in current:
                current[l] = {}
                current[l]['/'] = [{"path": path, "line_num": line_num, "offset": offset}]
            elif len(current[l]['/']) <= 5:  # TODO: < 5
                current[l]['/'].append({"path": path, "line_num": line_num, "offset": offset})
            current = current[l]

    def search(self, prefix):  # startsWith
        current = self.child
        for l in prefix:
            if l not in current:
                return []
            current = current[l]
        return current['/']


    # def search(self, prefix):
    #     rec_search(self, self.child,)
    #
    #
    # def rec_search(self, sentence, current, ):
    #     if sentence == ""
    #     if len(current) == 1:
    #         return current, # ... TODO:


