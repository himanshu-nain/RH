# MEDIC CARE
*"Ab Digital India Karega Care"*

Primitive HealthCare Solution For Remote Areas.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python Packages
```
Python3, mongoengine, reportlab, flask, flask-API
```
Database
```
MongoDB
```



### Installing

1. Clone Project
2. Populate mongoDB by running following command in terminal/cmd 
```
mongoimport --db Health --collection disease --file out.json
```
3. Run the project using
```
python3 Hack_app.py
```

## Deployment

You can deploy api contained in app.py to connect with different platforms. Change db address accordingly

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
