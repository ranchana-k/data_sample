import os
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
    files = os.listdir(os.path.join(parent_dir,'data_sample'))
    if files:
        return True
    else: 
        processed_files = os.listdir(os.path.join(parent_dir, 'processed'))
        if processed_files:
            return True
        else:
            return False


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
