class CsvOps():
    def __init__(self):
        pass

    ## Read csv file 
    #  @param fName name of file to read
    #  @return Array of entries
    def read_file(self, fName):
        with fName.open(fName) as f:
            for line in f.readLines():
                pass