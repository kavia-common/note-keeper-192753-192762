#!/bin/bash
cd /tmp/kavia/workspace/code-generation/note-keeper-192753-192762/django_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

