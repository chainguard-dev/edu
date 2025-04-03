## Chaindocs - Chainguard Documentation Tools
Tools for documentation maintenance. 

## Installation

```shell
cd tools/chaindocs
composer install
```
## Usage

### Audit Summary

```shell
./chaindocs audit
```

### Get deprecated articles

```shell
./chaindocs audit --deprecated
```

### Get articles with invalid timestamps

```shell
./chaindocs audit --invalid
```

### Get top articles from analytics csv

```shell
./chaindocs audit topcontent data=input.csv
```

To get only deprecated articles from the csv, ordered by number of views:

```shell
./chaindocs audit topcontent data=input.csv --deprecated
```

### Export audit csv

Invalid
```shell
./chaindocs audit report --invalid output=audit.csv
```

Deprecated
```shell
./chaindocs audit report --deprecated output=audit.csv
```

Deprecated from CSV list, ordered by number of views
```shell
./chaindocs audit report --topcontent data=input.csv output=audit.csv
```
