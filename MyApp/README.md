## Project description:

Site for uploading and editing images.

###### For details you can read the [Task](https://www.notion.so/backend-14c451038c5541c9996095192db75fc6).



## HOW TO INSTALL:

### Python version -- 3.8.5


#### 1) Activate your virtual environment:

##### For UNIX based systems:
```python
python3 -m venv venv
source venv/bin/activate
```

##### For Windows:
```python
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```


#### 2) Clone the repository to your local machine:

```python
git clone https://github.com/oldevgeny/upload-and-edit-images-django.git
```


#### 3) Install the requirements:

```python
pip install --upgrade pip
pip install -r requirements.txt
```


#### 4) Apply the migrations:

```python
python manage.py migrate
```



## START:

#### Run the development server:

```python
python manage.py runserver
```

###### The project will be available at http://127.0.0.1:8000/images/
