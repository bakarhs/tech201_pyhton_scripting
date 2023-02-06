import os
import subprocess

# Python doesn't actually run shell commands
# Instead we can use Python to run shell script files

scripts_dir = os.path.dirname(__file__)

script_absolute_path = os.path.join(scripts_dir + "script.sh")

subprocess.call(["sh", script_absolute_path])




