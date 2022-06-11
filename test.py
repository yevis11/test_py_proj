import requests
import pprint
import pytest
import allure
@pytest.fixture
def attach_text_finalize(request):
    allure.attach('a text attachment in module', 'thist is attachment text', allure.attachment_type.TEXT)
    def fin():
        allure.attach('A text attachment finalizer', 'this is finalize text', allure.attachment_type.TEXT)
    request.addfinalizer(fin)

@allure.severity('Trivial')
@allure.issue('jira link')
@allure.testcase('link to testlink')
@allure.story('Test story ')
def test_success():
    assert True

@allure.severity('Trivial')
@allure.issue('jira link')
@allure.testcase('link to testlink')
@allure.story('Test story ')
@allure.severity('Hard')
def test_failure():
    assert False

@allure.severity('Trivial')
@allure.issue('jira link')
@allure.testcase('link to testlink')
@allure.story('Test story ')
@allure.severity('Medium')
def test_skip():
    pytest.skip('reason')

@allure.severity('Trivial')
@allure.issue('jira link')
@allure.testcase('link to testlink')
@allure.story('Test story ')
@allure.severity('Low')
def test_broken():
    raise Exception('broken')


def test_one(attach_text_finalize):
    with allure.step('Step 1'):
        assert 10 == 10
    with allure.step("Step 2"):
        assert 1 != 1

@allure.severity('Trivial')
@allure.issue('jira link')
@allure.testcase('link to testlink')
@allure.story('Test story ')
@allure.severity('Medium')
def test_skip():
    pytest.skip('reason')