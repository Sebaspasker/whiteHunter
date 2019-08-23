import os

def path_creator(file):
        file_path = os.path.join(os.getcwd(), file)
        if not os.path.isfile(file_path):
            raise Exception("This is not a valid template path %s"%(file_path))
        return file_path