# node-hop

Simple program to hop into an ec2 instance by `tag:Name`.

## Usage

```
cd src/
pip3 install -r requirements.txt
./awsssh.py {{tag_name}}
```

## Unit testing

Very basic unit tests are included.

```
cd src/
python3 test.py
```

## Shortcomings

* Does not account for scenarios when multiple instances are tagged with the same name.
* Only can ssh into public hosts.