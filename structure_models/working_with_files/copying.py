import glob, os, shutil

class CopyMaker: 
    def copy(self, pathfrom, pathto, fileTemplate):
        files = glob.iglob(os.path.join(pathfrom, fileTemplate))
        for file in files:
            if os.path.isfile(file):
                shutil.copy(file, pathto)
                print "Files successfully copied. Well done, my friend!"
        
fromwhere = raw_input("Type path to the folder from where you want to copy files: ")
towhere = raw_input("Type path to the folder where you want to put copied files: ")
what = raw_input("Type name of the file you want to copy: ")
CopyMaker().copy(fromwhere, towhere, what)




