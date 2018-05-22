# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Script name: ShpToZip
#
# Description: A Python module to automate the conversion of .shp files to .zip
#              archives.
#
# Shp_to_Zip_README file includes the following information:
#              Project information - Script description - Software framework
#              Version control - Executing - Contributors - Licence - References
#
# Meta information: v.02.01 | 21 OCT 2017 | deepVector (author)
#-------------------------------------------------------------------------------

# Import system module(s)
import sys
import os
import glob
import zipfile

# Folder and file management:


def ShpToZipInDir(dirOut):
    # Check that the input folder exists
    if not os.path.exists(dirOut):
        print "ERROR: Input folder '%s' does not exist" % dirOut
        return False

    # If the output folder does not exist, create it
    dirOut_Zip = (dirOut + '_Zip')
    if not os.path.exists(dirOut_Zip):
        os.makedirs(dirOut_Zip)

    # Loop through .shp files in the input folder
    for inShp in glob.glob(os.path.join(dirOut, "*.shp")):
        # Build the .zip filename from the .shp filename
        outZip = os.path.join(
            dirOut_Zip, os.path.splitext(os.path.basename(inShp))[0] + ".zip")

        # Convert the .shp files to .zip files
        zipShp(inShp, outZip)
    return True


# Zipping:


def zipShp(inShpFile, newZipFN):
    # check if the input .shp exists
    if not (os.path.exists(inShpFile)):
        print "    ERROR: '%s' does not exist" % inShpFile
        return False

    # if the output .zip exists, delete it
    if (os.path.exists(newZipFN)):
        os.remove(newZipFN)

    # If the output .zip still exists, exit
    if (os.path.exists(newZipFN)):
        print "    ERROR: Unable to delete '%s'" % newZipFN
        return False

    # Open zip file object
    zipobj = zipfile.ZipFile(newZipFN, 'w')

    # Loop through .shp components
    for infile in glob.glob(inShpFile.lower().replace(".shp", ".*")):
        # Skip .zip file extension
        if os.path.splitext(infile)[1].lower() != ".zip":
            # Zip the .shp components
            zipobj.write(infile, os.path.basename(infile),
                         zipfile.ZIP_DEFLATED)

    # Close the .zip file object
    zipobj.close()
    return True


# To run the script standalone, uncomment and enter the path to 'dirOut':
# if __name__ == "__main__":
#    dirOut = "C:\\01\\output"
#    ShpToZipInDir(dirOut)
