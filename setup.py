import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__      = "0.0.0"
REPO_NAME        = 'TEXT_SUMMARIZATION_-PROJECT'
AUTHOR_USER_NAME = 'vivek-yogi'
SRC_REPO         = 'textSummarizer'
AUTHOR_EMAIL     = 'vivek87yogi@gmail.com'

setuptools.setup(
    name                     = SRC_REPO,
    version                  = __version__,
    author                   = AUTHOR_USER_NAME,
    author_email             = AUTHOR_EMAIL,
    description              = "A small python package for NLP app",
    Long_description         = long_description,
    Long_description_content = 'text/markdown',
    url                      = f"https://github.com/vivek-yogi/Text_summarizer_-project",
    project_url              = {
        "Bug Tracker ": f"https://github.com/vivek-yogi/Text_summarizer_-project/issues",},
    package_dir              = {"":"src"},
    packages                 = setuptools.find_packages(where='src')

)
