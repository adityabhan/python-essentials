import os

imdir = ''
if not os.path.isdir(imdir):
    os.mkdir(imdir)

#fidget_folders = [folder for folder in os.listdir('.') ]

n = 1
#for folder in fidget_folders:
for imfile in os.scandir(imdir):
    os.rename(imfile.path, os.path.join(imdir, '{:}.png'.format(n)))
    n += 1