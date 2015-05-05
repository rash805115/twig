import sys
import cx_Freeze

sys.path.append("twig")

base = None
if sys.platform == "win32":
	base = "Win32GUI"

cx_Freeze.setup(
	name = "Twig",
        version = "0.0",
        description = "Desktop software for bookeeping.",
	executables = [cx_Freeze.Executable("twig/service/start.py", base = base, targetName = "twig.exe")]
)

# import setuptools
# 
# setuptools.setup(
#         name = "Twig",
#         version = 0.0,
#         url = "https://github.com/rash805115/twig",
#         author = "Rahul Chaudhary",
#         author_email = "rahul300chaudhary400@gmail.com",
#         description = "Desktop software for bookeeping.",
#         install_requires = ["PySide == 1.2.2", "pybookeeping == 0.0.0"]
# )