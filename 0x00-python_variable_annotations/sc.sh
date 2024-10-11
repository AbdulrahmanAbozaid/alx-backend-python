# Array containing task numbers and file names
declare -A tasks=(
    ["0-add.py"]='#!/usr/bin/env python3\n\ndef add(a: float, b: float) -> float:\n    """Add two floats and return the sum."""\n    return a + b\n'
    ["1-concat.py"]='#!/usr/bin/env python3\n\ndef concat(str1: str, str2: str) -> str:\n    """Concatenate two strings and return the result."""\n    return str1 + str2\n'
    ["2-floor.py"]='#!/usr/bin/env python3\n\nimport math\n\ndef floor(n: float) -> int:\n    """Return the floor of a float."""\n    return math.floor(n)\n'
    ["3-to_str.py"]='#!/usr/bin/env python3\n\ndef to_str(n: float) -> str:\n    """Convert a float to its string representation."""\n    return str(n)\n'
    ["4-define_variables.py"]='#!/usr/bin/env python3\n\na: int = 1\npi: float = 3.14\ni_understand_annotations: bool = True\nschool: str = "Holberton"\n'
    ["5-sum_list.py"]='#!/usr/bin/env python3\n\nfrom typing import List\n\ndef sum_list(input_list: List[float]) -> float:\n    """Return the sum of a list of floats."""\n    return sum(input_list)\n'
    ["6-sum_mixed_list.py"]='#!/usr/bin/env python3\n\nfrom typing import List, Union\n\ndef sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:\n    """Return the sum of a list of integers and floats."""\n    return sum(mxd_lst)\n'
    ["7-to_kv.py"]='#!/usr/bin/env python3\n\nfrom typing import Union, Tuple\n\ndef to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:\n    """Return a tuple with the string and the square of the int/float."""\n    return (k, float(v**2))\n'
    ["8-make_multiplier.py"]='#!/usr/bin/env python3\n\nfrom typing import Callable\n\ndef make_multiplier(multiplier: float) -> Callable[[float], float]:\n    """Return a function that multiplies a float by a given multiplier."""\n    return lambda x: x * multiplier\n'
    ["9-element_length.py"]='#!/usr/bin/env python3\n\nfrom typing import Iterable, Sequence, List, Tuple\n\ndef element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:\n    """Return a list of tuples with sequences and their lengths."""\n    return [(i, len(i)) for i in lst]\n'
)

# Create files and add content to each one
for file in "${!tasks[@]}"; do
    echo -e "${tasks[$file]}" > "$file"
    chmod +x "$file"  # Make the file executable
done

echo "All files created and made executable."