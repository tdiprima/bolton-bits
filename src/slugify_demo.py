# slugify_demo.py
# Uses boltons.strutils.slugify to convert strings to URL-friendly slugs.
# Handles spaces, special characters, and case normalization automatically.

from boltons.strutils import slugify

print(slugify("Hello World!"))  # hello_world
