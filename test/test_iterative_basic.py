import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from unittest.mock import patch

print("Iterative: Should run successfully with 3 calls to input() for a 1-room house")
with patch("builtins.input", side_effect=[1, 1, 1]) as input_patch:
    with patch("builtins.print") as print_patch:
        import house_iterative

        assert input_patch.call_count == 3
        print_patch.assert_called()
print("OK")
