# Application to advertise product sales
## Objectives

The objective is to develop an application for registration of.

products and these products are listed for purchase and sales.

## Functionalities:

- Anyone can advertise products to be sold.
- Anyone can place orders for the advertised products.

### A Person has:
1. Name
2. email
3. Telephone
4. Address

### A product has:
1. Name
2. Details
3. Price
4. Availability (yes/no)

### An order has:
1. Product
2. Person who is placing
3. Amount
4. Delivery address
5. The order can be delivered or picked up

Each user will have a list of orders received ` my sales ` and orders made ` my purchases `.
1. The order must be accepted by the seller
2. The buyer will be able to track their orders:
3. Status: (Done, Accepted)

## How to start
#### 1. Locally
1. Install Python 3.8
```terminal
sudo apt install python3.9
```
2. Install Pip
```terminal
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## Stack
- [Fastpapi](https://fastapi.tiangolo.com/)
- [Python 3.8](https://docs.python.org/3.8/)
