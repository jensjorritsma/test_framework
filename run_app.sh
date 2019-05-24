if [[ ${1} = "debug" ]]; then
  export FLASK_ENV=development
  flask run
else
  export FLASK_ENV=production
  flask run
fi
