# VIVO translations property check

Compare the i18n properties files of VIVO/Vitro to a property file with translations. Output the original file minus the existing keys, with line breaks/comments intact.

## Usage

    python check_property_file.py ORIGINAL_FILE TRANSLATED_FILE [OUTPUT_FILE]

## Testing
Testing is done with [Pytest](http://pytest.org):

    py.test test_translationcheck.py