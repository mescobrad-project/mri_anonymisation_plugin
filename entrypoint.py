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
                    if 'ReferencedPatientSequence' in dcmdata:
                        dcmdata.ReferencedPatientSequence = None
                    if 'ReferencedSOPClassUID' in dcmdata:
                        dcmdata.ReferencedSOPClassUID = None
                    if 'ReferencedSOPInstanceUID' in dcmdata:
                        dcmdata.ReferencedSOPInstanceUID = None
                    if 'PatientName' in dcmdata:
                        dcmdata.PatientName = None
                    if 'PatientID' in dcmdata:
                        dcmdata.PatientID = None
                    if 'IssuerOfPatientID' in dcmdata:
                        dcmdata.IssuerOfPatientID = None
                    if 'TypeOfPatientID' in dcmdata:
                        dcmdata.TypeOfPatientID = None
                    if 'IssuerOfPatientIDQualifiersSequence' in dcmdata:
                        dcmdata.IssuerOfPatientIDQualifiersSequence = None
                    if 'UniversalEntityID' in dcmdata:
                        dcmdata.UniversalEntityID = None
                    if 'UniversalEntityIDType' in dcmdata:
                        dcmdata.UniversalEntityIDType = None
                    if 'IdentifierTypeCode' in dcmdata:
                        dcmdata.IdentifierTypeCode = None
                    if 'AssigningFacilitySequence' in dcmdata:
                        dcmdata.AssigningFacilitySequence = None
                    if 'LocalNamespaceEntityID' in dcmdata:
                        dcmdata.LocalNamespaceEntityID = None
                    if 'UniversalEntityID' in dcmdata:
                        dcmdata.UniversalEntityID = None
                    if 'UniversalEntityIDType' in dcmdata:
                        dcmdata.UniversalEntityIDType = None
                    if 'AssigningJurisdictionCodeSequence' in dcmdata:
                        dcmdata.AssigningJurisdictionCodeSequence = None
                    if 'CodeValue' in dcmdata:
                        dcmdata.CodeValue = None
                    if 'CodingSchemeDesignator' in dcmdata:
                        dcmdata.CodingSchemeDesignator = None
                    if 'CodingSchemeVersion' in dcmdata:
                        dcmdata.CodingSchemeVersion = None
                    if 'CodeMeaning' in dcmdata:
                        dcmdata.CodeMeaning = None
                    if 'MappingResource' in dcmdata:
                        dcmdata.MappingResource = None
                    if 'ContextGroupVersion' in dcmdata:
                        dcmdata.ContextGroupVersion = None
                    if 'ContextGroupLocalVersion' in dcmdata:
                        dcmdata.ContextGroupLocalVersion = None
                    if 'ContextGroupExtensionFlag' in dcmdata:
                        dcmdata.ContextGroupExtensionFlag = None
                    if 'ContextGroupExtensionCreatorUID' in dcmdata:
                        dcmdata.ContextGroupExtensionCreatorUID = None
                    if 'ContextIdentifier' in dcmdata:
                        dcmdata.ContextIdentifier = None
                    if 'ContextUID' in dcmdata:
                        dcmdata.ContextUID = None
                    if 'MappingResourceUID' in dcmdata:
                        dcmdata.MappingResourceUID = None
                    if 'LongCodeValue' in dcmdata:
                        dcmdata.LongCodeValue = None
                    if 'URNCodeValue' in dcmdata:
                        dcmdata.URNCodeValue = None
                    if 'EquivalentCodeSequence' in dcmdata:
                        dcmdata.EquivalentCodeSequence = None
                    if 'MappingResourceName' in dcmdata:
                        dcmdata.MappingResourceName = None
                    if 'AssigningAgencyOrDepartmentCodeSequence' in dcmdata:
                        dcmdata.AssigningAgencyOrDepartmentCodeSequence = None
                    if 'SourcePatientGroupIdentificationSequence' in dcmdata:
                        dcmdata.SourcePatientGroupIdentificationSequence = None
                    if 'GroupOfPatientsIdentificationSequence' in dcmdata:
                        dcmdata.GroupOfPatientsIdentificationSequence = None
                    if 'SubjectRelativePositionInImage' in dcmdata:
                        dcmdata.SubjectRelativePositionInImage = None
                    if 'PatientPosition' in dcmdata:
                        dcmdata.PatientPosition = None
                    if 'PatientBirthDate' in dcmdata:
                        dcmdata.PatientBirthDate = None
                    if 'PatientBirthTime' in dcmdata:
                        dcmdata.PatientBirthTime = None
                    if 'PatientBirthDateInAlternativeCalendar' in dcmdata:
                        dcmdata.PatientBirthDateInAlternativeCalendar = None
                    if 'PatientDeathDateInAlternativeCalendar' in dcmdata:
                        dcmdata.PatientDeathDateInAlternativeCalendar = None
                    if 'PatientAlternativeCalendar' in dcmdata:
                        dcmdata.PatientAlternativeCalendar = None
                    if 'PatientSex' in dcmdata:
                        dcmdata.PatientSex = None
                    if 'QualityControlSubject' in dcmdata:
                        dcmdata.QualityControlSubject = None
                    if 'StrainDescription' in dcmdata:
                        dcmdata.StrainDescription = None
                    if 'StrainNomenclature' in dcmdata:
                        dcmdata.StrainNomenclature = None
                    if 'StrainStockSequence' in dcmdata:
                        dcmdata.StrainStockSequence = None
                    if 'StrainStockNumber' in dcmdata:
                        dcmdata.StrainStockNumber = None
                    if 'StrainSourceRegistryCodeSequence' in dcmdata:
                        dcmdata = None
                    if 'StrainSource' in dcmdata:
                        dcmdata.StrainSource = None
                    if 'StrainAdditionalInformation' in dcmdata:
                        dcmdata.StrainAdditionalInformation = None
                    if 'StrainCodeSequence' in dcmdata:
                        dcmdata.StrainCodeSequence = None
                    if 'GeneticModificationsSequence' in dcmdata:
                        dcmdata.GeneticModificationsSequence = None
                    if 'GeneticModificationsDescription' in dcmdata:
                        dcmdata.GeneticModificationsDescription = None
                    if 'GeneticModificationsNomenclature' in dcmdata:
                        dcmdata.GeneticModificationsNomenclature = None
                    if 'GeneticModificationsCodeSequence' in dcmdata:
                        dcmdata.GeneticModificationsCodeSequence = None
                    if 'OtherPatientNames' in dcmdata:
                        dcmdata.OtherPatientNames = None
                    if 'OtherPatientIDsSequence' in dcmdata:
                        dcmdata.OtherPatientIDsSequence = None
                    if 'ReferencedPatientPhotoSequence' in dcmdata:
                        dcmdata.ReferencedPatientPhotoSequence = None
                    if 'ReferencedFrameNumber' in dcmdata:
                        dcmdata.ReferencedFrameNumber = None
                    if 'HL7InstanceIdentifier' in dcmdata:
                        dcmdata.HL7InstanceIdentifier = None
                    if 'ReferencedSegmentNumber' in dcmdata:
                        dcmdata.ReferencedSegmentNumber = None
                    if 'StudyInstanceUID' in dcmdata:
                        dcmdata.StudyInstanceUID = None
                    if 'SeriesInstanceUID' in dcmdata:
                        dcmdata.SeriesInstanceUID = None
                    if 'TypeOfInstances' in dcmdata:
                        dcmdata.TypeOfInstances = None
                    if 'DICOMRetrievalSequence' in dcmdata:
                        dcmdata.DICOMRetrievalSequence = None
                    if 'RetrieveAETitle' in dcmdata:
                        dcmdata.RetrieveAETitle = None
                    if 'DICOMMediaRetrievalSequence' in dcmdata:
                        dcmdata.DICOMMediaRetrievalSequence = None
                    if 'StorageMediaFileSetID' in dcmdata:
                        dcmdata.StorageMediaFileSetID = None
                    if 'StorageMediaFileSetUID' in dcmdata:
                        dcmdata.StorageMediaFileSetUID = None
                    if 'WADORetrievalSequence' in dcmdata:
                        dcmdata.WADORetrievalSequence = None
                    if 'RetrieveURI' in dcmdata:
                        dcmdata.RetrieveURI = None
                    if 'XDSRetrievalSequence' in dcmdata:
                        dcmdata.XDSRetrievalSequence = None
                    if 'RepositoryUniqueID' in dcmdata:
                        dcmdata.RepositoryUniqueID = None
                    if 'HomeCommunityID' in dcmdata:
                        dcmdata.HomeCommunityID = None
                    if 'WADORSRetrievalSequence' in dcmdata:
                        dcmdata.WADORSRetrievalSequence = None
                    if 'RetrieveURL' in dcmdata:
                        dcmdata.RetrieveURL = None
                    if 'EthnicGroup' in dcmdata:
                        dcmdata.EthnicGroup = None
                    if 'PatientSpeciesDescription' in dcmdata:
                        dcmdata.PatientSpeciesDescription = None
                    if 'PatientSpeciesCodeSequence' in dcmdata:
                        dcmdata.PatientSpeciesCodeSequence = None
                    if 'PatientBreedDescription' in dcmdata:
                        dcmdata.PatientBreedDescription = None
                    if 'PatientBreedCodeSequence' in dcmdata:
                        dcmdata.PatientBreedCodeSequence = None
                    if 'BreedRegistrationSequence' in dcmdata:
                        dcmdata.BreedRegistrationSequence = None
                    if 'BreedRegistrationNumber' in dcmdata:
                        dcmdata.BreedRegistrationNumber = None
                    if 'BreedRegistryCodeSequence' in dcmdata:
                        dcmdata.BreedRegistryCodeSequence = None
                    if 'ResponsiblePerson' in dcmdata:
                        dcmdata.ResponsiblePerson = None
                    if 'ResponsiblePersonRole' in dcmdata:
                        dcmdata.ResponsiblePersonRole = None
                    if 'ResponsibleOrganization' in dcmdata:
                        dcmdata.ResponsibleOrganization = None
                    if 'PatientComments' in dcmdata:
                        dcmdata.PatientComments = None
                    if 'PatientIdentityRemoved' in dcmdata:
                        dcmdata.PatientIdentityRemoved = None
                    if 'DeidentificationMethod' in dcmdata:
                        dcmdata.DeidentificationMethod = None
                    if 'DeidentificationMethodCodeSequence' in dcmdata:
                        dcmdata.DeidentificationMethodCodeSequence = None
                    if 'AdmittingDiagnosesDescription' in dcmdata:
                        dcmdata.AdmittingDiagnosesDescription = None
                    if 'AdmittingDiagnosesCodeSequence' in dcmdata:
                        dcmdata.AdmittingDiagnosesCodeSequence = None
                    if 'PatientAge' in dcmdata:
                        dcmdata.PatientAge = None
                    if 'PatientSize' in dcmdata:
                        dcmdata.PatientSize = None
                    if 'PatientSizeCodeSequence' in dcmdata:
                        dcmdata.PatientSizeCodeSequence = None
                    if 'PatientBodyMassIndex' in dcmdata:
                        dcmdata.PatientBodyMassIndex = None
                    if 'MeasuredAPDimension' in dcmdata:
                        dcmdata.MeasuredAPDimension = None
                    if 'MeasuredLateralDimension' in dcmdata:
                        dcmdata.MeasuredLateralDimension = None
                    if 'PatientWeight' in dcmdata:
                        dcmdata.PatientWeight = None
                    if 'MedicalAlerts' in dcmdata:
                        dcmdata.MedicalAlerts = None
                    if 'Allergies' in dcmdata:
                        dcmdata.Allergies = None
                    if 'Occupation' in dcmdata:
                        dcmdata.Occupation = None
                    if 'SmokingStatus' in dcmdata:
                        dcmdata.SmokingStatus = None
                    if 'AdditionalPatientHistory' in dcmdata:
                        dcmdata.AdditionalPatientHistory = None
                    if 'PregnancyStatus' in dcmdata:
                        dcmdata.PregnancyStatus = None
                    if 'LastMenstrualDate' in dcmdata:
                        dcmdata.LastMenstrualDate = None
                    if 'PatientSexNeutered' in dcmdata:
                        dcmdata.PatientSexNeutered = None
                    if 'ReasonForVisit' in dcmdata:
                        dcmdata.ReasonForVisit = None
                    if 'ReasonForVisitCodeSequence' in dcmdata:
                        dcmdata.ReasonForVisitCodeSequence = None
                    if 'AdmissionID' in dcmdata:
                        dcmdata.AdmissionID = None
                    if 'IssuerOfAdmissionIDSequence' in dcmdata:
                        dcmdata.IssuerOfAdmissionIDSequence = None
                    if 'ServiceEpisodeID' in dcmdata:
                        dcmdata.ServiceEpisodeID = None
                    if 'ServiceEpisodeDescription' in dcmdata:
                        dcmdata.ServiceEpisodeDescription = None
                    if 'IssuerOfServiceEpisodeIDSequence' in dcmdata:
                        dcmdata.IssuerOfServiceEpisodeIDSequence = None
                    if 'PatientState' in dcmdata:
                        dcmdata.PatientState = None
                    if 'ReferencedImageSequence' in dcmdata:
                        dcmdata.ReferencedImageSequence=None
                    if 'ProcedureCodeSequence' in dcmdata:
                        dcmdata.ProcedureCodeSequence = None


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

        return PluginActionResponse(None, None, name_of_anonymized_files,
                                    input_meta.data_info)
