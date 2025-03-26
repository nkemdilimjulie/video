A view is the Django **management command** which acts as a script that initiates the task. One view (a "class" or "def") initiates a task at the console.

### To switch from the Celery terminal (where it's connected to Redis and waiting for tasks) back to a new Bash terminal to run the Django server, follow one of these methods: 


*There are three methods. But method 1 is recommended.*

(If you can, open a new terminal tab or window (Method 1). It keeps Celery and Django running separately so you can **monitor logs for both**.)

**Method 1**: Open a New Terminal Tab/Window - **(Work on two separate terminals IN SEPARATE SCREENS)**
If using a terminal emulator (like GNOME Terminal, Konsole, etc.):

Press Ctrl + Shift + T (to open a new tab) OR

Press Ctrl + Shift + N (to open a new window).

Navigate to your project directory:

bash
Copy
Edit
cd ~/P24-E04/PROJECT\ IDEAS/video_enhancement_tools
Activate the virtual environment:

bash
Copy
Edit
source .videovenv/bin/activate
Run Django server:

bash
Copy
Edit
python manage.py runserver

**Method 2**: Use tmux or screen for Multiple Sessions - **(Work on two separate terminals IN ONE SCREEN)**
If you're using SSH or need to manage multiple processes in one terminal, use tmux or screen:

Start a tmux session:

bash
Copy
Edit
tmux
Run Celery in one session.

Open a new tmux pane (Ctrl + B, then % for vertical split or " for horizontal split).

In the new pane, navigate to the project folder and run python manage.py runserver.

To switch between panes:
Use Ctrl + B, then Arrow keys or Ctrl + B then O.

To detach from tmux (keep everything running in the background):

bash
Copy
Edit
Ctrl + B, then D
To reattach later:

bash
Copy
Edit
tmux attach

**Method 3**: Run Django Server in the Background - **(Work on two separate terminals BUT ONE SCREEN SHALL BE HIDDEN** In this particular case, CELERY screen shall be hidden.
If you don't want to open a new terminal, you can run Celery in the background and free up the terminal:

Stop Celery (Ctrl + C) if it’s running in the foreground.

Run Celery in the background using:

bash
Copy
Edit
celery -A video_enhancement_tools worker --loglevel=info &
The & at the end runs the command in the background.

Now you can use the same terminal to start Django:

bash
Copy
Edit
python manage.py runserver