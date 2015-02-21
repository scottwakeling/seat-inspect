from distutils.core import setup

setup(name = "seat-inspect",
      version = "1.0",
      description = "Understand and troubleshoot the login/seat system.",
      author = "Enrico Zini",
      author_email = "enrico@debian.org",
      url = "https://github.com/spanezz/seat-inspect",
      scripts = ["seat-inspect"],
      data_files = [ ("share/doc/seat-inspect", ["seat-inspect.html"]),
                     ("share/man/man1", ["seat-inspect.1"])] )
