import os
import shutil
if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(data,*args, **kwargs):
    """
    Args:
        data: The output from the upstream parent block (if applicable)
        args: The output from any additional upstream blocks

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    parent_dir = '/home/src' #'/home/src/bakcup 2022.12.13/bakcup 2022.12.13/test'
    if 'archived' not in os.listdir(parent_dir):
        os.mkdir(os.path.join(parent_dir,'archived'))
    files = data[1]
    for path in files:
        src_path = os.path.join(parent_dir,'processed',path)
        dest_path = os.path.join(parent_dir,'archived',path)
        shutil.move(src_path,dest_path)
    return True


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
