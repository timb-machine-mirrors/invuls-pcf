release: echo 'DELETE_ALL' | python new_initiation.py; python app.py
web: if [ "$FIRST_START" = "1" ] then python new_initiation.py fi; python app.py