Simple WebApp made by Noe Condado-Lino

Steps needed to run the applicaiton

1. Create and activate a Python virtual environment with using conda

        conda create -n "webApp" python=3.9.0
        
        conda activate "webApp"



2. Install dependencies

        pip install -r requirements.txt

3. Initialize the database

         python query.py


4. Run the application (NOTE: YOU MUST INITIALIZE DATABASE TO VIEW USERS ON APPLICATION)

         python wsgi.py


5. Access the application
   
    Open your browser and go to: http://127.0.0.1:5000
    
    Available routes:
    Homepage: http://127.0.0.1:5000/ 

    About: http://127.0.0.1:5000/about

    Users List: http://127.0.0.1:5000/users

    Or you can click the URL when you type the command in step 4 as it'll prompt you the URL

Troubleshooting

If you encounter any issues:
1. Make sure your virtual environment is activated
2. Verify the database is initialized by running python query.py
3. Check that all dependencies are installed correctly
4. Ensure you're running the commands from the project root directory