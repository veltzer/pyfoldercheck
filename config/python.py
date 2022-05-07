import config.project

package_name = config.project.project_name

console_scripts = [
    "pyfoldercheck=pyfoldercheck.main:main",
]

install_requires = [
    "pytconf",
    "pylogconf",
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "pymakehelper",
    "flake8",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
