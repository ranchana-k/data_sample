import os
import shutil
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    parent_dir = '/home/src' #'/home/src/bakcup 2022.12.13/bakcup 2022.12.13/test'
    #parent_dir = r'C:\Users\ranchana.kir_prinven\bakcup 2022.12.13\bakcup 2022.12.13\test'
    src_folder = os.path.join(parent_dir,'data_sample')
    dest_folder = os.path.join(parent_dir, 'processed')
    if 'processed' not in os.listdir(parent_dir):
        os.mkdir(os.path.join(parent_dir,'processed'))
    files = os.listdir(src_folder)
    process_files = []
    if files:
        
        for filename in files:
            src_filepath = os.path.join(src_folder, filename)
            dest_filepath = os.path.join(dest_folder, filename)
            shutil.move(src_filepath, dest_filepath)
            process_files.append(filename)
    else: 
        files = os.listdir(os.path.join(parent_dir,'processed'))
        #for filename in files:
        #    filepath = os.path.join(dest_folder, filename)
        process_files = files
        
    return [dest_folder, process_files]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
