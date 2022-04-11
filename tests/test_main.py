from m5py import dummy


def test_dummy():
    assert dummy() == "hello"
