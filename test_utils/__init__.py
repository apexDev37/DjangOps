"""Test utilities module.

This module is created to house utils commonly used across multiple test
modules (ie. factoryboy factories, base test classes, helper functions).

Rationale:
Since pytest discourages adding __init__.py files to test directories
(which makes them packages), importing directly from the tests directory can be
problematic. By placing shared utilities in this dedicated module, we can import
them easily without encountering import issues.

Usage:
Place any test-specific utilities in this module to ensure they can be reused
across different test files without duplication.

Note:
In some projects, this directory might be named `testing` or similar to indicate
its purpose.
"""
