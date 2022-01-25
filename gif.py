import os
import imageio

def make_gif(fpath,outpath,typ):
    '''make gif
    fpath : file path ,type : str,
    outpath : output file path ,type : str,
    typ : file extension,type : str. For example:jpg,png'''
    images = []
    for i in range(0,len(os.listdir(fpath))):
        filename=os.path.join(fpath,'{0}.{1}'.format(i,typ))
        images.append(imageio.imread(filename))
    imageio.mimsave(outpath, images)
    print('finish...')
if __name__=="__main__":
    # example
    fpath=r"C:\Users\x5748\Downloads\Path Planning_conti\fig"
    outpath='C:/Users/x5748/Downloads/ppo.gif'
    make_gif(fpath,outpath,'png')
