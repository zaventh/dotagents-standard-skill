# Mirrors mdl's built-in "relaxed" style, with two project-specific overrides at
# the bottom. Kept as a local file because mdl cannot parameterize a rule from
# .mdlrc without one.
all
exclude_tag :whitespace
exclude_tag :line_length

exclude_rule 'MD006' # Lists at beginning of line
exclude_rule 'MD007' # List indentation
exclude_rule 'MD033' # Inline HTML
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD040' # Fenced code blocks should have a language specified
exclude_rule 'MD041' # First line in file should be a top level header
exclude_rule 'MD047' # File should end with a single newline character

# MD029: ordered-list numbering is intentional in the docs.
exclude_rule 'MD029'

# MD024: Keep a Changelog repeats "### Added" / "### Changed" under every release
# heading. Those duplicates sit under different parents, so allow them while
# still catching true sibling duplicates.
rule 'MD024', :allow_different_nesting => true
