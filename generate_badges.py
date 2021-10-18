import os
import argparse
import git
import urllib.parse
import re

"""
MAKE SURE THERE'S ALREADY A `en` LANGUAGE FOLDER.
""" 

class Badge:

    @staticmethod
    def new_common_badge_url(badge_name: str, badge_value: str, badge_color: str):
        return (
            "https://img.shields.io/badge/%s-%s-%s" % ( 
                urllib.parse.quote(badge_name.replace('-', '--'), safe=''), 
                urllib.parse.quote(badge_value, safe=''), 
                badge_color 
            )
        )

    @staticmethod
    def new_progress_badge_url(badge_name: str, total: int, passed: int ) -> str:
        progress = int(passed/total*100)
        color = "green" if (progress>=70) else "yellow" if (progress>=30) else "red"
        return Badge.new_common_badge_url(
            badge_name=badge_name,
            badge_value="%d%% %d/%d" % (
                progress,
                passed,
                total
            ),
            badge_color=color
        )

    @staticmethod
    def content_update_badge_url(content: str, badge_name: str, new_badge_url: str):
        regex = r"(\!\[%s\])\((.*?)\)" % badge_name
        subst = "\\1(%s)" % new_badge_url
        result = re.sub(regex, subst, content, 0, re.MULTILINE)
        finded = re.findall(regex, content, re.MULTILINE)
        new_line = content[1 : ].find("\n")
        if len(finded) > 0:
            return result
        else:
            return content[:new_line + 1] + "![%s](%s) \n" % (badge_name, new_badge_url) + content[new_line + 1:]


class ReadmeMD:

    def __init__(self, fname: str):
        self.fname = fname
        self.content = self.get_content()

    def get_content(self) -> str:
        return ReadmeMD.get_file_content(self.fname)

    def write_content(self, content: str):
        ReadmeMD.write_file_content(self.fname, content)
        self.content=content

    @staticmethod
    def get_file_content(fname: str) -> str:
        with open(fname, 'r') as f: 
            return f.read()

    @staticmethod
    def write_file_content(fname, content: str):
        with open(fname, 'w') as f: 
            f.write(content)

def generate(language: str):
    git_dir = git.Repo(search_parent_directories=True)
    parent_dir = git_dir.working_dir 
    language_dir = os.path.join(parent_dir, 'docs')
    readme_file = os.path.join(parent_dir, "README.md")
    readme = ReadmeMD(readme_file)
    
    if language not in os.listdir(language_dir):
        raise ValueError(f'language {language} not found')
    english_language_dir = os.path.join(language_dir, 'en')
    # README + index (which is outside the en dir) so added 2
    total_files = sum(len(files) for _, _, files in os.walk(english_language_dir)) + 2  
    
    language_dir = os.path.join(language_dir, language)
    num_files_language = sum(len(files) for _, _, files in os.walk(language_dir))
    readme_file = os.path.join(parent_dir, "README.md")
    readme = ReadmeMD(readme_file)

    readme.write_content(
            content=Badge.content_update_badge_url(
                content=readme.content,
                badge_name=language,
                new_badge_url=Badge.new_progress_badge_url(
                    badge_name=language,
                    total=total_files,
                    passed=num_files_language,
                )
            )
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", required=True)
    args = parser.parse_args()

    generate(args.language)
    

