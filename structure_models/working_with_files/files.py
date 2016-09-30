import os
class DSFileRemover: 
    def clean(self, path, fileTemplate):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file == fileTemplate:
                    os.remove(os.path.join(root, file))
                    print "File %s was successfully removed." % fileTemplate
