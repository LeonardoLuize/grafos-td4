class ReadFile:
  def readFilesLines(self, filename):
    with open(filename, "r") as newFile:
      return newFile.readlines()