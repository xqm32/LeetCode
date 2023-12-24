import datetime
import json
import os
import re
import subprocess
import sys
import textwrap
from typing import Self


class LeetCode:
    @classmethod
    def _exec(cls, command: list[str], **kwargs) -> None:
        print(f"lcmd[INFO]: executing `{' '.join(command)}`")
        proc: subprocess.CompletedProcess = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            **kwargs,
        )
        if proc.stdout is not None and len(proc.stdout) > 0:
            stdout: str = proc.stdout.strip("\n")

            stdout = f"\n{stdout}\n\n"
            stdout = textwrap.indent(stdout, "lcmd[INFO]:     ", lambda _: True)
            print(stdout, end="")

    def __init__(self: Self, config_path: str = "config.json") -> None:
        self.config_path: str = config_path
        if not os.path.isfile(config_path):
            print(f"lcmd[ERRO]: config file `{config_path}` not found")
            sys.exit(os.EX_CONFIG)
        with open(config_path, "r") as f:
            self.config: dict[str, str] = json.load(f)

        if (today := self.config.get("today")) is not None:
            print(f"lcmd[WARN]: loading `today` from `{self.config_path}`")
            self.year, self.month, self.day = today.split(".")
            self.today: str = today
        else:
            datetime_today: datetime.datetime = datetime.datetime.today()
            self.year, self.month, self.day = (
                str(datetime_today.year),
                str(datetime_today.month),
                str(datetime_today.day),
            )
            self.today: str = f"{self.year}.{self.month}.{self.day}"
        print(f"lcmd[INFO]: `today` is {self.today}")

    def finish(self) -> None:
        leetcode_path: str | None = self.config.get("leetcode")
        if leetcode_path is None:
            print(f"lcmd[ERRO]: please set `leetcode` in `{self.config_path}`")
            sys.exit(os.EX_CONFIG)

        if not os.path.isfile(f"{self.today}.py"):
            print(f"lcmd[ERRO]: file `{self.today}.py` not found")
            sys.exit(os.EX_NOINPUT)
        with open(f"{self.today}.py", "r") as f:
            py_content = f.read().strip("\n")
        leetcode_id = re.findall(r"^#.*id=(\d+).*$", py_content, re.MULTILINE)
        if len(leetcode_id) == 0:
            print(f"lcmd: leetcode id not found in `{self.today}.py`")
            sys.exit(os.EX_DATAERR)
        leetcode_id = leetcode_id[0]

        year_path: str = os.path.join(leetcode_path, self.year)
        if not os.path.isdir(year_path):
            os.mkdir(year_path)

        month_path: str = os.path.join(year_path, f"{self.month}.md")
        if not os.path.isfile(month_path):
            # create month file
            with open(month_path, "w") as f:
                f.flush()

        with open(month_path, "r") as f:
            content: list[str] = f.readlines()

        if f"# {self.today}\n" in content:
            print(f"lcmd[ERRO]: `{self.today}` already in `{month_path}`")
            sys.exit(os.EX_DATAERR)

        if len(content) < 4:
            print(f"lcmd[INFO]: writing to `{month_path}` with initial content")
            content: list[str] = [
                "---\n",
                f"title: {self.year}.{self.month}\n",
                "draft: false\n",
                "---\n",
            ]
            with open(month_path, "w") as f:
                f.writelines(content)

        content[4:4] = [
            "\n",
            f"# {self.today}\n",
            "\n",
            "```python\n",
            f"{py_content}\n",
            "```\n",
        ]
        with open(month_path, "w") as f:
            f.writelines(content)

        cwd = os.getcwd()
        os.chdir(leetcode_path)
        print(f"lcmd[INFO]: commit message: leetcode: finished #{leetcode_id}")
        choice: str = input("lcmd[INFO]: commit? [y/c/N] ")
        match choice:
            case "y" | "Y":
                self._exec(["git", "add", month_path])
                self._exec(
                    ["git", "commit", "-m", f"leetcode: finished #{leetcode_id}"]
                )
                self._exec(["git", "push"])
                os.chdir(cwd)
                self._exec(["mv", f"{self.today}.py", f"leetcode/{self.today}.py"])
            case "c" | "C":
                self._exec(["git", "checkout", month_path])
                print("lcmd[INFO]: commit canceled and checkout")
            case _:
                print("lcmd[INFO]: commit canceled")


if __name__ == "__main__":
    config_path: str | None = None
    if len(sys.argv) == 2:
        config_path = sys.argv[1]
    LeetCode(config_path=config_path).finish()
