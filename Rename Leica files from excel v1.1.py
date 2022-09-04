import pandas as pd
import os
import shutil
import glob

def from_excel (input_dir, plate_file, folder_name):
    plate_path= os.path.join(input_dir, plate_file)
    out_dir= os.path.join(input_dir, folder_name+'_Renamed')
    images_path= os.path.join(input_dir, folder_name)
    df= pd.read_excel(plate_path)
    os.chdir(images_path)
    files= glob.glob('*.tif')
    df.set_index('Row', inplace=True)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for file in files:
        if file!= plate_file:
            row= file.split('_')[-4]
            col= file.split('_')[-3]
            name= df.at[row, int(col)].split('_')[0]
            rep= df.at[row, int(col)].split('_')[2]
            conc= df.at[row, int(col)].split('_')[1]
            field= file.split('_')[-2]
            ch= file.split('_')[-1]
            new_name= name+'_'+conc+'_'+rep+'_'+field+'_'+ch
            new_path= os.path.join(out_dir, new_name)
            shutil.copy(file, out_dir)
            file_copy= os.path.join(out_dir,file)
            os.rename(file_copy, new_path)
    return


def from_excel_vert (input_dir, plate_file, folder_name):
    plate_path= os.path.join(input_dir, plate_file)
    out_dir= os.path.join(input_dir, folder_name+'_Renamed')
    images_path= os.path.join(input_dir, folder_name)
    df= pd.read_excel(plate_path)
    os.chdir(images_path)
    files= glob.glob('*.tif')
    df.set_index('Row', inplace=True)
    columns=list(df.columns)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    for file in files:
        if file!= plate_file:
            row= file.split('_')[-4]
            col= file.split('_')[-3]
            name= columns[int(col)-1].split('_')[0]
            rep= columns[int(col)-1].split('_')[1]
            conc= df.at[row, columns[int(col)-1]]
            field= file.split('_')[-2]
            ch= file.split('_')[-1]
            new_name= name+'_'+str(conc)+'_'+rep+'_'+field+'_'+ch
            new_path= os.path.join(out_dir, new_name)
            shutil.copy(file, out_dir)
            file_copy= os.path.join(out_dir,file)
            os.rename(file_copy, new_path)
    return

#files_dir= input('Folder path:')
files_dir= 'C:\\Lab\\Microscopy\\Jim ERKi\\A431 ERKi 24h 16-06-2022'
os.chdir(files_dir)
#files_dir= 'C:\\Lab\\Python\\temp\\test'
if not os.path.exists(files_dir):
    print('Folder does not exist')
#print('Rename functions: \n 1.each well named \n 2.vertical orientation')
#option= input('Select rename function:')
option = '1'
if option=='1':
    from_excel(files_dir, 'plate file.xlsx', 'Raw')
elif option=='2':
    from_excel_vert(files_dir, 'plate file.xlsx', 'Raw')
os.chdir('C:\\Lab\\Python')











    



