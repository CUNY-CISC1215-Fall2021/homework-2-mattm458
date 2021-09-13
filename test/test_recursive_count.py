import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from unittest import mock
from unittest.mock import patch

print("Recursive: Should request input 7 times for a 3-room house")
with patch("builtins.input", side_effect=[3, 5, 4, 3, 2, 1, 2]) as input_patch:
    with patch("builtins.print") as print_patch:
        import house_recursive

        assert input_patch.call_count == 7

print("OK")
