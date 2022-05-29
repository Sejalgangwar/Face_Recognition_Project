# Face Recognition Project
Microsoft Intern Engage Mentorship Program 2022 Project

## Project Description
This is a face recognition based security gate system to be installed at the entrance of an apartment.The details of the residents are stored. Whenever a person tries to enter the apartment, the security gate system detects his face. If he is a resident, his name is displayed by the face recognition system, else no recognition takes place. Only the residents are then allowed to enter the apartment. The names, entry time and entry date are recorded in a MySQL database.

## Steps to run the project
1. Install python-3.10.4 (64 bit) or above from https://www.python.org/downloads/ and add the PATH to your user and System Variables under Environment variables.

2. Install Pycharm Community Edition 2022.1.1 from https://www.jetbrains.com/pycharm/download/#section=windows and add the PATH to your user and System Variables under Environment variables.

3. Install the following libraries to run the code :
     * opencv-python (pip install opencv-python)
     * numpy (pip install numpy)
     * cmake (pip install cmake)
     * dlib (pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl)
     * face-recognition (pip install face-recognition)
     * pillow (pip install Pillow) 
5. Install MySQL8 from https://dev.mysql.com/downloads/installer/ 

5. Install MySQL Python connector (pip install mysql-connector-python)

6. Clone my git repository to a directory in your device using : git clone command.

7. Now run login.py from your pycharm ide. Enter username as **'sejalgangwar'** and password as **'Hookrux@912'** and login to the security gate.

8. Now you can view the residents information using 'Resident Details' button.

9. 'Get yourself verified' can be used to detect and recognize faces through the web cam of the people entering the apartment.

10. 'Entry Records' displays data of the people recognized through the web cam.
