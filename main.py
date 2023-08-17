import subprocess
import json
import os

if not "GITHUB_USERNAME" in os.environ:
    raise Exception("Environment variable GITHUB_USERNAME not defined.")

USER_NAME = os.environ["GITHUB_USERNAME"]
print(f"Github username is set to {USER_NAME}")

proc = subprocess.Popen(
    ["gh repo list -L 1000 --json name"], stdout=subprocess.PIPE, shell=True
)
(out, err) = proc.communicate()

repos = json.loads(out.decode("utf-8"))

for repo in repos:
    full_name = f'{USER_NAME}/{repo["name"]}'
    answer = input(f"Delete {full_name}? (y/n): ")
    if answer == "y":
        proc = subprocess.Popen(
            [f"gh repo delete {full_name} --yes"], stdout=subprocess.PIPE, shell=True
        )
        print(f"{full_name} was deleted.")
