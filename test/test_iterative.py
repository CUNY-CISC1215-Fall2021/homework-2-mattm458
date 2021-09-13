import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from unittest.mock import patch

print(
    "Iterative: Should output 'Your home is 28 square feet' with 3 rooms of an appropriate size"
)
with patch("builtins.input", side_effect=[3, 5, 4, 3, 2, 1, 2]) as input_patch:
    with patch("builtins.print") as print_patch:
        import house_iterative

        print_patch.assert_any_call("Your home is 28 square feet")
print("OK")
