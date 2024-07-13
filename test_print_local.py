import requests
import pytest
import sys
import io


if len(sys.argv) != 2:
    print("Usage: python script.py <DROPBOX_URL>")
    sys.exit(1)

# Read the direct download link of the Dropbox file from the command line argument
dropbox_url = sys.argv[1]

# Download the test script content
response = requests.get(dropbox_url)
if response.status_code != 200:
    raise ValueError("Failed to download test script from Dropbox.")
test_script_content = response.text

# Use exec to dynamically execute the test script content
exec(test_script_content)

# Capture pytest output
stdout = io.StringIO()
stderr = io.StringIO()
sys_stdout = sys.stdout
sys_stderr = sys.stderr

try:
    sys.stdout = stdout
    sys.stderr = stderr
    result = pytest.main(["-v"])
finally:
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr

# Print pytest results
print(stdout.getvalue())
print(stderr.getvalue())