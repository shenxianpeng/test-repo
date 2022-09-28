import os
from pathlib import Path

link = Path(os.path.expanduser("~/.local/bin/")) / ("clang-format")
print(link)

target = "/usr/lib/llvm-12/bin/clang-format"
install_os = "linux"

try:
    link.symlink_to(target)
    print("symbolic link created", str(link))
    
except OSError as exc:  # pragma: no cover
    print(
        "Encountered an error when trying to create the symbolic link:",
        "; ".join([x for x in exc.args if isinstance(x, str)]),
        sep="\n    ",
    )
    print(exc)
