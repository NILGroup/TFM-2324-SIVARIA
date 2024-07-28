import os
import math
from datetime import datetime
#Own created modules
from ..expert_system import constants

class FileManager(object):


    def getFilesDir(self, folder):
        directory = constants.FILEPATH + folder
        files = os.listdir(directory)
        total = len(files)

        return (total, files)


    def removeSaveFile(self, filename):
        modelType = filename.split('_')[1]
        filePath = constants.FILEPATH + modelType + '/' + filename
        if os.path.exists(filePath) == False:
            raise FileNotFoundError('Filename not found. Type the name correctly.\n\n' + self.getHelpMessage())

        os.remove(filePath)

    def getConfigModelFilename(self, modelType):
        now = datetime.now()
        versionDateTime = now.strftime("%Y%m%d%H%M%S")
        filePath = constants.FILEPATH + modelType
        filename = filePath + '/' + 'model_' + modelType + '_' + versionDateTime + constants.MODEL_FILETYPE

        return (filePath, filename)

    def getMostRecentFile(self, modelType):

        try:
            filePath = constants.FILEPATH + modelType + '/'
            #print(filePath)
            listFiles = os.listdir(filePath)
            listFiles.sort(reverse=True)    
            #print(listFiles)

            return (filePath + listFiles[0])
        except Exception:
            return None

    def getFileInfo(self, filename):
        fileStats = self.getFileStats(filename)

        fileInfoStr = 'File: ' + filename + '\n'

        fileInfoStr += 'File size: ' + str(fileStats['st_size']) + ' ' + fileStats['st_size_unit'] + '\n'
        fileInfoStr += 'Most recent access: ' + str(fileStats['st_atime']) + '\n'
        fileInfoStr += 'Most recent content change: ' + str(fileStats['st_mtime']) + '\n'
        fileInfoStr += 'Most recent metadata change: ' + str(fileStats['st_ctime']) + '\n'

        return fileInfoStr

    def getFileStats(self, filename):
        fileStats = os.stat(filename)

        st_size, unit = self.convertSize(fileStats.st_size)

        return {
            'filename': filename,
            'st_atime': self.convertSecondsToDatetime(fileStats.st_atime),
            'st_mtime': self.convertSecondsToDatetime(fileStats.st_mtime),
            'st_ctime': self.convertSecondsToDatetime(fileStats.st_ctime),
            'st_size': st_size,
            'st_size_unit': unit,
        }
    
    def convertSize(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return (s, size_name[i])

    def convertSecondsToDatetime(self, st_time):
        return datetime.fromtimestamp(st_time).strftime('%d-%m-%Y %H:%M:%S')
