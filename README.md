# ![](./img/deepVector_logo_100.png)

# ShpToZip
The utility script *ShpToZip.py* automates the task of converting ArcGIS .shp files to .zip archives.

The script was developed for **Geospatial Data Analysis**: UBC course [external link](http://mgem.forestry.ubc.ca/courses/gem-530/)

# Table of Contents

- Software framework
- Version control
- Executing
- Contributors
- Licence
- References

<!-- /TOC -->
## Software framework
*   **Required software** (version used during development)
 *   **Python** (v. 2.7) - Python Programming Language [(external link)](https://www.python.org/)
*   **Optional software** (version used during development)
 *   **Git** (v. 2.14.2) - Version history [(external link)](https://git-scm.com/)

## Version control
Version (date): **01.02** (15 OCT 2017)

Versionining was performed with Git.  To review version history, the folder *17ubcCgem530_Lab04_Repo* can be opened in Git as a repository.

## Executing
To execute as a module, copy *ShpToZip.py* (along with associated files *ShpToZip_README.md* and *ShpToZip_LICENCE.md*) to the folder containing the calling script.  The module can be called with the following parameters:

    # Import module
    import ShpToZip

    # Location of the folder that contains the output .shp files
    dirOut = "C:\\folderName"

    # Execute module
    ShpToZip.ShpToZipInDir(dirOut)

## Contributors
*   Witold Ciolkiewicz - Author
* Code elements adapted from:
 * mafic9 *et al.* (2015)
 * Esri (2017)
 * Greer (2017)

## Licence
This script is licensed under the terms of the MIT Licence (see [*LICENCE.md*](LICENCE.md)).

## References
Esri, 2017, Zip (compress) Python script, online: https://desktop.arcgis.com/en/arcmap/latest/analyze/sharing-workflows/h-zip-python-script.htm [accessed 14 October 2017].

Greer, B., 2017, Zip all shapefiles in directory individually, online: http://www.bgcarto.com/zip-all-shapefiles-in-directory-individually/[accessed 14 October 2017].

mafic9, Hornbydd, lpugh01, oogalabs1, johnswood, hzhu, and yooperjb, 2015, Zipping multiple shapefiles to multiple zip folders, online: https://community.esri.com/thread/28985 [accessed 14 October 2017].
