# test

A small dummy project used for testing code-exploration agents.

## Structure

```
src/
  models.py    – User, Product, and Order domain classes
  utils.py     – Standalone utility functions (email validation, clamp, etc.)
  services.py  – Service layer that ties models and utilities together

tests/
  test_models.py    – pytest tests for models
  test_utils.py     – pytest tests for utilities
  test_services.py  – pytest tests for services

js/
  helpers.js        – JavaScript helper functions
  helpers.test.js   – Lightweight JS tests (run with Node)

config.json         – Sample JSON configuration
config.yaml         – Sample YAML configuration
```

## Running Tests

**Python** (requires `pytest`):

```bash
pytest
```

**JavaScript**:

```bash
node js/helpers.test.js
```