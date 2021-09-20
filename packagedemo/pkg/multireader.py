import os 
from pkg.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class MultiReader:
    def __init__(self, filename):
        extension = os.path.split(filename)[1]
        opener = extension_map.get(extension, open)
        self.filename = filename
        self.f = open(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()