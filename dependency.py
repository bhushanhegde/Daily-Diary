#this program shoud run only once at the begining of instalation to create some files and directories.

import os
class dependency:

    def make_dirs(self):
        try:
            os.mkdir('logs')
            os.chdir('logs')
            os.mkdir('private')
            os.mkdir('professional')
        except:
            print('this file should be run only once when you install the application.')



if __name__=='__main__':
    d=dependency()
    d.make_dirs()
