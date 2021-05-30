We will deploy on Heroku the Flask project we did in the last project.

1. Copy the files of the web app in the current directory:  
   `app.py`, `index.html` and `model` <br><br>

2. Try to launch it using gunicorn  
   To execute in the project directory:

    ```
    pip install gunicorn
    gunicorn app:app
    ```

    Go to http://localhost:8000 and check it works  
    Then stop the server (Ctrl+C)<br><br>

2. Create `Procfile`  
   This will tell Heroku the command to launch the app

   ```
   echo 'web: gunicorn app:app -b 0.0.0.0:${PORT:-8000}' > Procfile
   ```

3. Create `requirements.txt`.  
   This will tell Heroku which packages to install

    ```
    pip install pipreqs

    # Dump the depencendies of the .py files
    pipreqs .

    # Add additional dependencies (model + server)
    echo sklearn >> requirements.txt
    echo gunicorn >> requirements.txt
    ```

   NB to check the dependencies of the pickled model:

    ```
    wget https://gist.githubusercontent.com/a-mt/258faf48c16778db36699a6af60889cb/raw/2762501014cc990f8c9a1441610b17210f1e7eb8/pickle_dependencies.py
    python pickle_dependencies.py --file model
    ```

4. Commit the files  
   To execute in the project 9 parent directory:

    ```
    git add "Project 9"
    git status
    git commit -m "Deploy Flask app on Heroku"
    ```

5. Create a Heroku app

    ```
    heroku login
    heroku create
    ```

6. Commit `Project 9` to Heroku

    ```
    git subtree push --prefix "Project 9" heroku master
    ```

   If you need to force commit:

   ```
   git push heroku `git subtree split --prefix "Project 9" master`:master --force
   ```

   Wait for Heroku to build the project.  
   Once you get the prompt back, follow the link to the web app and check that it works

   For this example, the app is deployed on  
   [https://obscure-gorge-18484.herokuapp.com/](https://obscure-gorge-18484.herokuapp.com/) 
