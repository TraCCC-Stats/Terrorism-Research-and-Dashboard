# Changelog

All notable changes to the *structure* of the data files included in this project will be documented in this file.

Examples of structural changes may include adding or removing fields, reordering fields, or casting fields as a different data type.

This file does not include data changes (e.g. the addition, deletion, or updates of records).

## [1.6.0] 2024-09-18

### Added

- A `suspected` column was added to the PERPS report, indicating whether the listed perpetrator is suspected of commiting the incident rather than confirmed

## [1.5.0] 2024-03-28

### Added

- Fields beginning with `Pcat` were added to the PERPS table.

## [1.4.0] 2024-02-28

### Added

- `latitude` and `longitude` columns to INCIDENTS and PERPS exports

## [1.3.0] 2023-11-29

### Added

- `2023_GRID_Codebook_V2.pdf` file

## [1.2.0] 2023-10-23

### Added

- `GTTAC Terms of Use and Citation Policy.pdf` file

## [1.1.0] 2023-03-27

### Added

- Added `country_nongenc_txt` field to the INCIDENTS and PERPS tables. In most cases this value will match `country_genc_txt`. However, there are currently three countries where these values will differ:
    - DEMOCRATIC REPUBLIC OF CONGO (listed as 'CONGO (KINSHASA)' in GENC)
    - MYANMAR (listed as 'BURMA' in GENC)
    - TÜRKIYE (listed as 'TURKEY' in GENC)

## [1.0.0] 2022-12-07

### Removed

- Fields beginning with `Pcat` in the PERPS table have been removed. These fields were duplicates of the `Icat` fields in the INCIDENTS table.
