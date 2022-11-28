# Application to advertise product sales
## Objectives

The objective is to develop an application for registration of
products and these products are listed for purchase and sales.

## Functionalities:

- Anyone can advertise products to be sold.
- Anyone can place orders of the advertised products.

### A User has:
1. Name
2. email
3. Telephone
4. Address

### A Product has:
1. Name
2. Details
3. Price
4. Availability (yes/no)

### An Order has:
1. Product
2. User who places the order
3. Quantity
4. Delivery address
5. The order can be delivered or picked up

Each user will have a list of orders received ` my sales ` and orders made ` my purchases `.
1. The order must be accepted by the user
2. The buyer will be able to track their orders:
3. Status: (Done, Accepted)

## How to start
#### 1. Locally
1. Install Python 3.8
```terminal
sudo apt install python3.8
```
2. Install Pip
```terminal
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
3. Install the packages using pip according to the requirements.tx file
```terminal
pip install -U -r requirements.txt
```
## Unit tests

Unit tests are created with the use of Pytest library (
[Link to documentation](https://docs.pytest.org/en/6.2.x/getting-started.html)
).
All unit test are placed in *`tests`* file.

To run all unit tests together:

```terminal
pytest -vs
```

## Stack
- [Fastpapi](https://fastapi.tiangolo.com/)
- [Python 3.8](https://docs.python.org/3.8/)
- [Sqlite](https://sqlitebrowser.org/dl/)
