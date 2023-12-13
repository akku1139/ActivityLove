if [ -n "$PYTHONPATH" ]; then
  add=":$PYTHONPATH"
fi

export PYTHONPATH="`cd $(dirname ${0}) && pwd`/src$add"
