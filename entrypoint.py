from mescobrad_edge.plugins.mri_anonymisation_plugin.models.plugin import EmptyPlugin, PluginActionResponse, PluginExchangeMetadata

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
                        dcmdata.PatientID = 'None'
                    if 'PatientName' in dcmdata:
                        dcmdata.PatientName = 'None'
                    if 'PatientSex' in dcmdata:
                        dcmdata.PatientSex = 'None'
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

    def deface_mri(self, method: str, path_to_files: str) -> None:
        import os
        import pydicom
        import sys
        import nibabel as nib
        import numpy as np

        dcmfolder = path_to_files
        outdir = path_to_files + "/defaced"

        # - Create outfolder
        os.makedirs(os.path.join(path_to_files,'defaced/tmpdeface'), exist_ok = True)

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
        cmd = 'dcm2niix '+str(idcm)
        self.run_cmd(cmd,"Error converting dicom to nifti file")

        t1w = [xx for xx in os.listdir(dcmfolder) if xx.endswith(".nii")]
        t1w = os.path.join(dcmfolder,t1w[0])

        # - Deface using Freesurfer
        if method == 'freesurfer':
            fshome = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files"
            print("Defacing...")
            outfile = os.path.join(outdir,'tmpdeface', 'defaced-nifti.nii')
            cmd = os.path.join(fshome, "mri_deface ")+t1w+" \
                                "+os.path.join(fshome,'talairach_mixed_with_skull.gca')+" \
                                "+os.path.join(fshome,'face.gca')+"\
                                "+outfile
            self.run_cmd(cmd,"Error DeFaceing T1w image")

        else:
            print(' Wrong defacing method. It has to be ')
            sys.exit()


        # - Convert Nifti to multiple DICOM files
        print(" Converting deFace Nifti into series of DICOM with same metadata")
        # Load one dicom file as reference
        refdcm = pydicom.dcmread(idcm)

        # Get image orientation encoded in dicom
        #(i.e which direction was used to aquire the multiple 2D slices)
        imgorient = refdcm.ImageOrientationPatient
        plane = np.round(imgorient)

        if (plane[0] == 1.)  and (plane[5] == -1.):
            slicedir = 'Coronal'
        elif (plane[1] == 1.)  and (plane[5] == -1.):
            slicedir = 'Sagittal'
        elif (plane[0] == 1.)  and (plane[4] == 1.):
            slicedir = 'Axial'
        else:
            print(" Invalid Image Orientation. We can not infer slice encoding direction")
            print(" Contact IT team")
            sys.exit(1)

        # Load Nifti image
        img = nib.load(os.path.join(outdir, 'tmpdeface', 'defaced-nifti.nii'))

        # Get all dicom files (and sort by name)
        dicomfiles = []
        for kk in os.listdir(dcmfolder):
            # Avoid non-dicom files within folder
            try:
                idcm = os.path.join(dcmfolder,kk)
                dcm = pydicom.dcmread(idcm)
                dicomfiles.append(idcm)
            except:
                continue

        # Store Nifti Slices from defaced file into a dicom file
        if slicedir == 'Coronal':
            # Reorient Nifti to have match with DICOM
            inorient = nib.io_orientation(img.affine)
            wantorient = nib.orientations.axcodes2ornt("LIP")
            transf_orient = nib.orientations.ornt_transform(inorient, wantorient)
            newimg = img.as_reoriented(transf_orient)
            nifti = newimg.get_fdata()

            # Loop over all 2D slices in the j-plane
            for idx,cdicom in enumerate(sorted(dicomfiles)):
                newdcm = pydicom.dcmread(cdicom)

                # Int to bytes conversion
                pixel_array = nifti[idx,:,:]
                pixel_array = pixel_array.astype(np.uint16)
                pixel_bytes = pixel_array.tobytes()

                # Store data into dicom file
                newdcm.PixelData = pixel_bytes

                # Write dicom file
                outf = os.path.join(outdir,'DCM-annon-'+str(idx).zfill(4))
                newdcm.save_as(outf)

        elif slicedir == 'Sagittal':
            # Reorient Nifti to have match with DICOM
            inorient = nib.io_orientation(img.affine)
            wantorient = nib.orientations.axcodes2ornt("LIP")
            transf_orient = nib.orientations.ornt_transform(inorient, wantorient)
            newimg = img.as_reoriented(transf_orient)
            nifti = newimg.get_fdata()

            # Loop over all 2D slices in the i-plane
            for idx,cdicom in enumerate(sorted(dicomfiles)):
                newdcm = pydicom.dcmread(cdicom)

                # Int to bytes conversion
                pixel_array = nifti[idx,:,:]
                pixel_array = pixel_array.astype(np.uint16)
                pixel_bytes = pixel_array.tobytes()

                # Store data into dicom file
                newdcm.PixelData = pixel_bytes

                # Write dicom file
                outf = os.path.join(outdir,'DCM-annon-'+str(idx).zfill(4))
                newdcm.save_as(outf)

        else:
            # Reorient Nifti to have match with DICOM
            inorient = nib.io_orientation(img.affine)
            wantorient = nib.orientations.axcodes2ornt("PIL")
            transf_orient = nib.orientations.ornt_transform(inorient, wantorient)
            newimg = img.as_reoriented(transf_orient)
            nifti = newimg.get_fdata()

            # Loop over all 2D slices in the z-plane
            for idx,cdicom in enumerate(sorted(dicomfiles)):
                newdcm = pydicom.dcmread(cdicom)

                # Int to bytes conversion
                pixel_array = nifti[:,idx,:]
                pixel_array = pixel_array.astype(np.uint16)
                pixel_bytes = pixel_array.tobytes()

                # Store data into dicom file
                newdcm.PixelData = pixel_bytes

                # Write dicom file
                outf = os.path.join(outdir,'DCM-annon-'+str(idx).zfill(4))
                newdcm.save_as(outf)


        print('======= Done defacing MRI data. =======')


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


        s3 = boto3.resource("s3",
                            endpoint_url=self.__OBJ_STORAGE_URL__,
                            aws_access_key_id=self.__OBJ_STORAGE_ACCESS_ID__,
                            aws_secret_access_key=self.__OBJ_STORAGE_ACCESS_SECRET__,
                            config=Config(signature_version='s3v4'),
                            region_name=self.__OBJ_STORAGE_REGION__)


        # Existing non annonymized data in local MinIO bucket
        bucket_local = s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)
        obj_personal_data = bucket_local.objects.filter(Prefix="mri_data/", Delimiter="/")

        # Existing anonymized data in data lake
        bucket = s3.Bucket(self.__OBJ_STORAGE_BUCKET__)
        obj_anonymous_data = bucket.objects.filter(Prefix="mri_anonymized_data/", Delimiter="/")

        keys_anonymous_data = [os.path.basename(obj.key) for obj in obj_anonymous_data]

        # Files which are not yet anonymized
        files_to_anonymize = [obj.key for obj in obj_personal_data if os.path.basename(obj.key) not in keys_anonymous_data]

        # Remove data directories if exists (Before download it is not expected to have data for processing inside this directory)
        for dir in os.listdir(deface_path):
            current_dir = os.path.join(deface_path, dir)
            if os.path.isdir(current_dir):
                shutil.rmtree(current_dir)

        # Download data which need to be defaced and anonymized
        for file_name in files_to_anonymize:
            path_zip_file = deface_path+os.path.basename(file_name)
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).download_file(file_name, path_zip_file)
            path_to_unzip = deface_path+os.path.basename(file_name).split('.')[0]
            with zipfile.ZipFile(path_zip_file, 'r') as zip_ref:
                zip_ref.extractall(path_to_unzip)

            # After extraction delete downloaded zip file
            os.remove(path_zip_file)

            # Move data from subfolder into parent folder to reduce redundant folders
            # If there is no subfolder, keep structure
            destination = path_to_unzip
            files_list = os.listdir(path_to_unzip)
            for filename in files_list:
                source = os.path.join(path_to_unzip, filename)
                if os.path.isdir(source):
                    files_to_move = os.listdir(source)
                    for files in files_to_move:
                        file = os.path.join(source, files)
                        shutil.move(file, destination)
                    shutil.rmtree(source)


    def upload_file(self, path_to_anonymized_files: str) -> None:
        import boto3
        from botocore.client import Config
        import os
        import shutil
        from zipfile import ZipFile, ZIP_STORED

        s3 = boto3.resource('s3',
                            endpoint_url= self.__OBJ_STORAGE_URL__,
                            aws_access_key_id= self.__OBJ_STORAGE_ACCESS_ID__,
                            aws_secret_access_key= self.__OBJ_STORAGE_ACCESS_SECRET__,
                            config=Config(signature_version='s3v4'),
                            region_name=self.__OBJ_STORAGE_REGION__)

        obj_name = os.path.basename(os.path.split(path_to_anonymized_files)[0])
        zip_name = os.path.split(path_to_anonymized_files)[0] + "/" + obj_name + "_final.zip"

        # Create zip file with defaced and anonymized data
        with ZipFile(zip_name, 'w', ZIP_STORED) as zipObj:
            # Iterate over all the files in directory
            for root, dirs, files in os.walk(path_to_anonymized_files):
                for file in files:
                    if file.endswith(".nii"):
                        continue

                    # create complete filepath of file in directory
                    file_path = os.path.join(root, file)

                    # Add file to zip
                    zipObj.write(file_path, os.path.basename(file_path), compress_type=ZIP_STORED)

        # Upload output zip file with defaced and anonymized data
        s3.Bucket(self.__OBJ_STORAGE_BUCKET__).upload_file(zip_name, "mri_anonymized_data/"+ obj_name + ".zip")

        # Remove data
        shutil.rmtree(os.path.split(path_to_anonymized_files)[0])

    def action(self, input_meta: PluginExchangeMetadata = None) -> PluginActionResponse:
        """Run defacing algorithm.
        Remove all personal metadata.
        """
        import os

        # Path where defaced data will be stored during defacing and anonymisation
        path_to_data = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"

        # Download data to process
        self.download_file(path_to_data)

        data_dirs = os.listdir(path_to_data)
        for dir in data_dirs:
            current_path = os.path.join(path_to_data, dir)
            if os.path.isdir(current_path):
                # Perform defacing
                self.deface_mri(method="freesurfer", path_to_files=current_path) # using method freesurfer mri_deface

                # Remove all personal information
                self.annon_mri(path_to_defaced_files=current_path+"/defaced")

                # Upload processed data
                self.upload_file(current_path+"/defaced")

        return PluginActionResponse()
