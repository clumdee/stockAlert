import os 
import sys
from pathlib import Path

# choose index such that file.parents[index] gives /project/
package_root_directory = Path(os.getcwd()).resolve().parents[0]
sys.path.append(str(package_root_directory))