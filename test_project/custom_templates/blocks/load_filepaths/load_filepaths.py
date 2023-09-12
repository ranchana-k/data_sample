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
    src_folder = './data_sample'
    dest_folder = './process'
    if 'process' not in os.listdir():
        os.mkdir('process')
    files = os.listdir(src_folder)
    for filename in files:
        src_filepath = src_folder + '/' + filename
        return src_filepath


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
