To connect to a database through a Jupyter notebook, we need to install several dependencies:

```
conda install sqlalchemy
conda install psycopg2
pip install ipython-sql
```

[SQLalchemy](http://www.sqlalchemy.org/) is a python package which allows to connect to different types of databases.

[psycopg2](http://initd.org/psycopg/) is a package needed to connect to a PostgreSQL database.

[ipython-sql](https://pypi.python.org/pypi/ipython-sql) is an ipython magic which allows us to directly type SQL commands in a Jupyter notebook.

To test your installation, you can run all cells of the [TestConnection.ipynb](./TestConnection.ipynb) Notebook. In the second cell you will have to substitute the word password with the real password you are provided in email.
