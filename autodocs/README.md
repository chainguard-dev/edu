## Autodocs Maintenance Tools
Tools for documentation maintenance. 

## Installation

```shell
cd autodocs
composer install
```
## Usage

### Audit Summary

```shell
./autodocs audit
```

### Get deprecated articles

```shell
./autodocs audit --deprecated
```

### Get articles with invalid timestamps

```shell
./autodocs audit --invalid
```

### Get top articles from analytics csv

```shell
./autodocs audit topcontent data=input.csv
```

To get only deprecated articles from the csv, ordered by number of views:

```shell
./autodocs audit topcontent data=input.csv --deprecated
```

### Export audit csv

Invalid
```shell
./autodocs audit report --invalid output=audit.csv
```

Deprecated
```shell
./autodocs audit report --deprecated output=audit.csv
```

Deprecated from CSV list, ordered by number of views
```shell
./autodocs audit report --topcontent data=input.csv output=audit.csv
```
