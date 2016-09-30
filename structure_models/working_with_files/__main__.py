from files import DSFileRemover

if __name__ == "__main__":
    where = raw_input("Type path to the folder you want to work with: ")
    what = raw_input("Type name of the file you want to delete: ")
    DSFileRemover().clean(where, what)