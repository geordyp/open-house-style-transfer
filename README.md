# open-house-style-transfer
Open house project for the SIGAI club

## Technologies Used
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PyTorch](http://pytorch.org/)
* [NumPy](http://www.numpy.org/)
* [SciPy](https://www.scipy.org/)
* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

For the full list of installs, view "pg_config.sh"

## Setup
* (Optional) If using vagrant, enter the command `vagrant up` from the directory containing "Vagrantfile" then enter the command `vagrant ssh` followed by `cd /vagrant/`.  


1. Change to the "mysite" directory: `cd mysite`
2. Apply all migrations: `python3 manage.py migrate`
3. Run the server: `python3 manage.py runserver 0:5000`
4. Open a browser and navigate to "localhost:5000/styletransfer/"
