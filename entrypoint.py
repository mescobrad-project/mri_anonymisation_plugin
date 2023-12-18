from mescobrad_edge.plugins.mri_anonymisation_plugin.models.plugin import EmptyPlugin,\
      PluginActionResponse, PluginExchangeMetadata

class GenericPlugin(EmptyPlugin):
    def annon_mri(self, path_to_defaced_files: str) -> None:
        import os
        import pydicom
        """
        1. Search all dcm images
        2. Annon main fields
        3. Save annon data
        """
        # Parse info
        print("Working with data subject " + path_to_defaced_files)
        cpath = path_to_defaced_files
        outpath=cpath
        os.makedirs(outpath, exist_ok=True)

        # Loop over ALL files
        for root, dirs, files in os.walk(cpath):
            for cdcm in files:
                cdcm = os.path.join(root, cdcm)
                try:
                    dcmdata = pydicom.dcmread(cdcm)

                    # Several possible fields name. Need to check, add news
                    if 'PatientBirthDate' in dcmdata:
                        dcmdata.PatientBirthDate = None
                    if 'PatientID' in dcmdata:
                        dcmdata.PatientID = None
                    if 'PatientName' in dcmdata:
                        dcmdata.PatientName = None
                    if 'PatientSex' in dcmdata:
                        dcmdata.PatientSex = None
                    if 'PatientWeight' in dcmdata:
                        dcmdata.PatientWeight = None

                    # Save updated annon MRI
                    outfiletmp = cdcm
                    os.makedirs(os.path.dirname(outfiletmp), exist_ok = True)
                    dcmdata.save_as(outfiletmp)

                except:
                    continue
        print("======= Removed personal data. =======")

    def my_print(self,message):
        """
        print message, then flush stdout
        """
        import sys
        print(message)
        sys.stdout.flush()

    def run_cmd(self,cmd,err_msg):
        """
        execute the comand
        """
        import subprocess
        import sys
        self.my_print('#@# Command: ' + cmd+'\n')
        retcode = subprocess.Popen(cmd,shell=True, executable='/bin/bash').wait()
        if retcode != 0 :
            self.my_print('ERROR: '+err_msg)
            sys.exit(1)
        self.my_print('\n')

    def deface_mri(self, method: str, path_to_files: str, outdir_path: str) -> None:
        import os
        import pydicom
        import sys
        import nibabel as nib
        import numpy as np

        dcmfolder = path_to_files
        outdir = os.path.join(outdir_path, "defaced")

        # - Create outfolder
        os.makedirs(os.path.join(outdir_path,'defaced/tmpdeface'), exist_ok = True)

        # - Convert dicom to nifti
        print("Converting dicom to nifti...")
        for kk in os.listdir(dcmfolder):
            # Avoid non-dicom files within folder
            try:
                idcm = os.path.join(dcmfolder,kk)
                dcm = pydicom.dcmread(idcm)
                break
            except:
                continue

        print(".  Using dicom: "+idcm)

        try: # convert original DICOM  file into NIfTI file
            cmd = 'dcm2niix ' + str(idcm)
            self.run_cmd(cmd, "Error converting dicom to nifti file")

        except: # in case of specific DICOM it needs to be first converted into new DICOM
            # file with gdcmconv tool and then continue with conversion into NIfTI file

            out_folder = os.path.join(dcmfolder, 'gdcm_convert')
            for fn in os.listdir(dcmfolder):
                if not os.path.exists(out_folder):
                    os.makedirs(out_folder)
                idcm = os.path.join(dcmfolder, fn)
                odcm = os.path.join(out_folder, fn + "_gdcm")

                # convert DICOM to DICOM file
                cmd_gdcmconv = f"gdcmconv --jpeg {idcm} {odcm}"
                self.run_cmd(cmd_gdcmconv, "Error converting dicom to dicom file")

            # converted DICOMs convert to NIfTI
            cmd_dcm2niix = f'dcm2niix -o {dcmfolder} {odcm}'
            self.run_cmd(cmd_dcm2niix, "Error converting gdcm dicom to nifti file")



        t1w = [xx for xx in os.listdir(dcmfolder) if xx.endswith(".nii")]
        t1w = os.path.join(dcmfolder,t1w[0])

        # - Deface using Freesurfer
        if method == 'freesurfer':
            fshome = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer"
            subjects_dir = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"
            mideface_path = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer/bin/mideface"

            outfile_mgz = os.path.join(path_to_files, 'example.mgz')
            outfile_defaced_mgz = os.path.join(outdir, 'example_defaced.mgz')
            outfile_defaced_nifti = os.path.join(outdir, 'tmpdeface', 'defaced-nifti.nii')
            qa = os.path.join(outdir, 'qa')

            print("Defacing...")

            # Run the mideface algorithm
            # a) Set Freesurfer path
            # b) Run setup script
            # c) Set path to the data directory
            # d) Convert nifti to mgz format required for mideface
            # e) Run mideface algorithm
            # f) Convert output mgz to nifti

            cmd = f"export FREESURFER_HOME={fshome}" \
                + " && source $FREESURFER_HOME/SetUpFreeSurfer.sh" \
                + f" && export SUBJECTS_DIR={subjects_dir}" \
                + f" && mri_convert {t1w} {outfile_mgz}" \
                + f" && {mideface_path} --i {outfile_mgz} --o {outfile_defaced_mgz} --odir {qa}" \
                + f" && mri_convert {outfile_defaced_mgz} {outfile_defaced_nifti}"

            self.run_cmd(cmd,"Error DeFaceing image")

            print('======= Done defacing MRI data. =======')

        else:
            print(' Wrong defacing method. It has to be ')
            sys.exit()

    def download_file(self, deface_path: str) -> None:
        import boto3
        from botocore.client import Config
        import zipfile
        import os
        import shutil

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)

        # Existing non annonymized data in local MinIO bucket
        bucket_local = s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)
        obj_personal_data = bucket_local.objects.filter(Prefix="mri_data/", Delimiter="/")

        # Files which are not yet anonymized
        files_to_anonymize = [obj.key for obj in obj_personal_data]

        # Remove data directories and zip files if exists
        # Before download it is not expected to have data for processing inside this
        # directory
        for item in os.listdir(deface_path):
            current_item = os.path.join(deface_path, item)
            if os.path.isdir(current_item):
                shutil.rmtree(current_item)
            if item.endswith(".tmp.part"):
                os.remove(current_item)

        # Download data which need to be defaced and anonymized
        for file_name in files_to_anonymize:
            path_zip_file = deface_path+os.path.basename(file_name)

            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)\
                .download_file(file_name, path_zip_file)

            # Delete original file in local storage
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).\
                objects.filter(Prefix=file_name).delete()

            with zipfile.ZipFile(path_zip_file, 'r') as zip_ref:
                # Get the list of all items in the ZIP archive
                zip_contents = zip_ref.namelist()

                # Check if any item in the root directory is a file
                contains_files = any('/' not in item for item in zip_contents)
                if contains_files:
                    path_to_unzip=deface_path + os.path.basename(file_name).split(".")[0]
                else:
                    path_to_unzip=deface_path

                zip_ref.extractall(path_to_unzip)

            # After extraction delete downloaded zip file
            os.remove(path_zip_file)

    def upload_file(self, path_to_anonymized_files: str) -> None:
        import boto3
        from botocore.client import Config
        import os
        import shutil
        from zipfile import ZipFile, ZIP_STORED
        import time

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)


        obj_name = os.path.split(path_to_anonymized_files)[1]
        zip_name = os.path.split(path_to_anonymized_files)[0] + "/" + obj_name + \
            "_final.zip"

        # Create zip file with defaced and anonymized data
        with ZipFile(zip_name, 'w', ZIP_STORED) as zipObj:
            # Iterate over all the files in directory
            for root, dirs, files in os.walk(path_to_anonymized_files):
                for file in files:
                    if file.endswith('.nii'):
                        # create complete filepath of file in directory
                        file_path = os.path.join(root, file)
                        basename_zip = os.path.basename(path_to_anonymized_files)
                        second_part_of_zip_name = root.split(basename_zip)[1]
                        name_in_zipped_file = basename_zip + \
                            os.path.split(second_part_of_zip_name)[0]
                        name_in_zipped_file = os.path.join(name_in_zipped_file, file)

                        # Add file to zip
                        zipObj.write(file_path, name_in_zipped_file, compress_type=ZIP_STORED)
                    else:
                        continue

        # Upload output zip file with defaced and anonymized data
        ts = round(time.time()*1000)
        folder_name = "MRIs"
        name_of_file_minio = f"{folder_name}/{obj_name}_{ts}.zip"
        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_file(zip_name,
                                                                       name_of_file_minio)

        # Remove data
        shutil.rmtree(os.path.split(path_to_anonymized_files)[0])

        print('======= File is uploaded to the local storage. =======')

        return name_of_file_minio

    def ignore_files(self, dir, files):
        import os
        return [f for f in files if os.path.isfile(os.path.join(dir, f))]


    def reproduce_directory_tree(self, path_to_files, path_to_copied_structure):
        """Create the copy of the data structure, ignoring the files."""
        import shutil
        shutil.copytree(path_to_files,
                        path_to_copied_structure,
                        ignore=self.ignore_files)

    def deidentify_files(self, path_to_files, outdir):
        """Iterate through data structure, and for each directory
        consisted of DICOM files perform defacing and anonymization."""

        import os
        import logging
        import shutil

        basename = os.path.basename(path_to_files)
        for root, dirs, files in os.walk(path_to_files):
            if files: # check if there are files within current directory
                current_basename = root.split(basename)[1]
                outdir_path = outdir + current_basename
                try:
                    # Remove all personal information
                    self.annon_mri(path_to_defaced_files=os.path.join(root))

                    # Perform defacing
                    self.deface_mri("freesurfer", os.path.join(root), outdir_path)

                except: # if some error occurs during deidentification remove output of
                    # current data and just continue with other datasets
                    shutil.rmtree(os.path.join(outdir_path, "defaced"))
                    logging.error("Impossible to deidentify files within {} folder"\
                                  .format(basename+current_basename))
                    continue
            else: # if there are no files, just continue on another level,
                # to find directory which have files
                continue

    def action(self, input_meta: PluginExchangeMetadata = None) -> PluginActionResponse:
        """Run defacing algorithm.
        Remove all personal metadata.
        """
        import os

        # Path where original and defaced data will be stored during defacing and
        # anonymisation
        path_to_data = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"

        # Download data to process
        self.download_file(path_to_data)

        name_of_anonymized_files = []
        data_dirs = os.listdir(path_to_data)

        for dir in data_dirs:
            current_path = os.path.join(path_to_data, dir)

            if os.path.isdir(current_path):
                path_to_copied_structure = os.path.join(path_to_data, "deidentified",
                                                        dir)
                self.reproduce_directory_tree(current_path, path_to_copied_structure)

                # Perform defacing and anonymisation of the DICOM files
                self.deidentify_files(current_path, path_to_copied_structure)

                # Upload processed data
                name_of_file = self.upload_file(path_to_copied_structure)

                name_of_anonymized_files.append(name_of_file)

        return PluginActionResponse(None, None, name_of_anonymized_files)