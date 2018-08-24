#!/usr/bin/bash
for f in *.py; do
  echo "$f"
  python "$f" localhost:50051 > /dev/null &
done
