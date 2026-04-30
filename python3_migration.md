# Changes made in the migration to Python 3

This document summarizes the changes applied to the project to update it from Python 2 to Python 3 and to review compatibility with CherryPy.

## Changes from Python 2 to Python 3

Language structures used in Python 2 were updated:

- Replacement of `except Exception, e` with `except Exception as e`.
- Replacement of `basestring` with `str`.
- Replacement of `long(...)` with `int(...)`.
- Replacement of `cPickle` with `pickle`.
- Changes in relative imports so they work correctly as packages in Python 3.

## Changes in imports and packages

Several imports were adjusted so Python 3 resolves them correctly:

- In `src/webapp`
- In `src/webapp/html`
- In `src/webapp/html/components`
- In `src/webapp/html/output`
- In `src/barleymapcore/alignment`
- In `src/barleymapcore/annotators`
- In `src/barleymapcore/datasets`
- In `src/barleymapcore/maps`
- In `src/barleymapcore/maps/enrichment`
- In `src/barleymapcore/maps/reader`

## Changes related to CherryPy

- The project’s compatibility with CherryPy 18.x was reviewed.
- The code was adapted to work with Python 3.

## Specific functional changes

### `src/webapp/Bmap.py`

- Adaptation of input types (`str` instead of `basestring`).
- Fix for handling uploaded files in Python 3

### `src/webapp/RunQuery.py`

- Update of `except` blocks
- Compatibility with relative imports in Python 3

### `src/barleymapcore/maps/reader/MappingsParser.py`

- Replacement of `cPickle` with `pickle`.
- Change to reading the serialized index in binary mode (`rb`).

### `src/barleymapcore/db/GraphsConfig.py`

- Adjustment for lists returned by dictionaries in Python 3.

## Startup script

The `_START` script was updated to allow the application to run with Python 3.

```bash
python3 ./src/server.py
```
