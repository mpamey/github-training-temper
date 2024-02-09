from src.functions.my_functions import add_integers, subtract_column_integers
import pandas as pd


class TestAddIntegers:
    def test_add_integers(self):
        # Arrange
        x = 1
        y = 2
        expected = 3

        # Act
        output = add_integers(x, y)

        # Assert
        assert output == expected

    def test_add_integers_negative(self):
        # Arrange
        x = -1
        y = -2
        expected = -3

        # Act
        output = add_integers(x, y)

        # Assert
        assert output == expected

    def test_subtract_column_integers(self):
        # Arrange
        sample = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
            }
        )
        expected = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                "Subtracted": [-3, -3, -3],
            }
        )

        # Act
        output = subtract_column_integers(sample, "A", "B")

        # Assert
        pd.testing.assert_frame_equal(output, expected)
        assert (sample.dtypes == expected.dtypes).all()
