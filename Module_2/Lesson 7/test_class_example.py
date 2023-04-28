from class_example import custom_compress

INCOMING_ITERABLE = "I HATELOVE UNIT TESTING"
SELECTORS = [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
EXPECTED_RESULT = list("I LOVE UNIT TESTING")


def test_custom_compress():
    result = list(custom_compress(INCOMING_ITERABLE, SELECTORS))
    assert result == EXPECTED_RESULT
