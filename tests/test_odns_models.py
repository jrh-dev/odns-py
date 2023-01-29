from odns.all_packages import all_packages
import pytest

@pytest.mark.vcr()
def test_return():
    """ Tests all_packages returns expected result """
    res = all_packages(limit=2)
    assert len(res) == 2
    assert res[0][0] == 'e8d82157-1870-4458-9dc0-0e17e113e6c1'
    assert res[0][1] == 'quarterly-epidemiological-data-on-healthcare-associated-infections'
    assert res[1][0] == 'f9bab568-501e-49d3-a0a4-0b9a7578b0de'
    assert res[1][1] == 'child-and-adolescent-mental-health-waiting-times'

@pytest.mark.vcr()
def test_fail():
    """ Tests all_packages fails when passed bad """
    with pytest.raises(Exception):
        res = all_packages(limit="a")

