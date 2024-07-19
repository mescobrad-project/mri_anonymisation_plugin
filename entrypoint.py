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

    def find_T1w(self, json_metadata):
        """Among all NIfTI files detect ones for T1w"""

        criteria_combinations = [
            {'Manufacturer': 'Philips', 'SeriesDescription': 'T1',
             'PulseSequenceName': 'T1TFE', 'MRAcquisitionType': '3D',
             'ScanningSequence': 'GR'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'T1',
             'PulseSequenceName': 'TIR', 'MRAcquisitionType': '2D',
             'ScanningSequence': 'IR'}, #not sure if necessary
            {'Manufacturer': 'Philips', 'SeriesDescription': 'T1',
             'PulseSequenceName': 'SE', 'MRAcquisitionType': '3D',
             'ScanningSequence': 'SE'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'T1',
             'PulseSequenceName': '', 'MRAcquisitionType': '', 'ScanningSequence': 'SE'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'T1',
             'PulseSequenceName': '', 'MRAcquisitionType': '2D',
             'ScanningSequence': 'SE'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'T1',
             'PulseSequenceDetails': 'tse_vfl', 'MRAcquisitionType': '3D',
             'ScanningSequence': 'SE'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'mprage',
             'PulseSequenceDetails': 'tse_vfl', 'MRAcquisitionType': '3D',
             'ScanningSequence': 'SE'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'T1',
             'MRAcquisitionType': '3D', 'ScanningSequence': 'GR'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'mprage',
             'MRAcquisitionType': '3D', 'ScanningSequence': 'GR'},
            {'Manufacturer': 'GE', 'SeriesDescription': 't1',
             'PulseSequenceName': 'BRAVO', 'MRAcquisitionType': '3D',
             'ScanningSequence': 'GR'}
        ]

        # exclusion strings for SeriesDescription:
        exclusion_strings = ['GAD', 'GD'] #normally T1w is scanned with and without Gd

        verdicts = []

        # Iterate over each JSON file in the directory
        for index, row in json_metadata.iterrows():
            # Convert field values to lowercase for case-insensitive comparison
            data_lower = {key: value.lower() if isinstance(value, str) else value \
                          for key, value in row.items()}

            # Check each criteria combination
            verdict = 0
            for criteria in criteria_combinations:
                criteria_lower = {key: value.lower() if isinstance(value, str) \
                                  else value for key, value in criteria.items()}
                if all(criteria_value.lower() in data_lower.get(criteria_key, '').lower()
                       for criteria_key, criteria_value in criteria_lower.items()):

                    # Check if field2 contains any exclusion strings
                    if all(exclusion.lower() \
                           not in data_lower.get('SeriesDescription', '').lower() \
                           for exclusion in exclusion_strings):
                        # Exclude Processed images (e.g, MPR)
                        if (not any('PROJECTION' in s for s in data_lower.get('ImageType'))
                            and
                            not any('DERIVED' in s for s in data_lower.get('ImageType'))):
                            verdict = 1
                            print(data_lower.get('file_name'))
                            break

            verdicts.append(verdict)

        json_metadata['field_verdict'] = verdicts
        filtered_json_metadata = json_metadata[json_metadata['field_verdict'] == 1]
        return filtered_json_metadata

    def find_flair(self, json_metadata):
        """Among all MRI NIfTI sequences detect Flair ones"""

        criteria_combinations = [
            {'Manufacturer': 'Philips', 'SeriesDescription': 'FLAIR',
             'PulseSequenceName': 'TIR', 'ScanningSequence': 'IR'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'FLR',
             'PulseSequenceName': 'TIR', 'ScanningSequence': 'IR'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'FLAIR',
             'ScanningSequence': 'IR'},
            {'Manufacturer': 'Philips', 'SeriesDescription': 'FLR',
             'ScanningSequence': 'IR'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'FLAIR',
             'PulseSequenceDetails': 'tse', 'ScanningSequence': 'SE\IR'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'FLR',
             'PulseSequenceDetails': 'tse', 'ScanningSequence': 'SE\IR'},
            {'Manufacturer': 'Siemens', 'SeriesDescription': 'dark-fluid',
             'PulseSequenceDetails': 'tse', 'ScanningSequence': 'SE'},
            {'Manufacturer': 'GE', 'SeriesDescription': 'flair',
             'PulseSequenceName': 'T2FLAIR', 'ScanningSequence': 'SE'}
        ]

        # exclusion strings for SeriesDescription:
        exclusion_strings = ['HIPO', 'MIP', '1nsa']

        verdicts = []

        # Iterate over each JSON file in the directory
        for index, row in json_metadata.iterrows():
            # Convert field values to lowercase for case-insensitive comparison
            data_lower = {key: value.lower() if isinstance(value, str) else value \
                          for key, value in row.items()}

            # Check each criteria combination
            verdict = 0
            for criteria in criteria_combinations:
                criteria_lower = {key: value.lower() if isinstance(value, str) else value
                                  for key, value in criteria.items()}
                if all(criteria_value.lower() in data_lower.get(criteria_key, '').lower()
                       for criteria_key, criteria_value in criteria_lower.items()):

                    # Check if field2 contains any exclusion strings
                    if all(exclusion.lower()
                           not in data_lower.get('SeriesDescription', '').lower()
                           for exclusion in exclusion_strings):

                        # Exclude Processed images (e.g, MPR)
                        if (not any('PROJECTION' in s for s in data_lower.get('ImageType'))
                            or
                            not any('DERIVED' in s for s in data_lower.get('ImageType'))):
                            verdict = 2
                            print(data_lower.get('file_name'))
                            break

            verdicts.append(verdict)

        json_metadata['field_verdict'] = verdicts
        filtered_json_metadata = json_metadata[json_metadata['field_verdict'] == 2]
        return filtered_json_metadata


    def read_json_files(self, json_files_list):
        """Read json files to extract information needed to detect T1 or Flair sequince"""
        import pandas as pd
        import os
        import json

        df = pd.DataFrame()

        # Read each JSON file specified in the list
        for json_file_path in json_files_list:

            # Read the JSON file and convert to DataFrame
            with open(json_file_path, 'r') as json_file:
                json_data = json.load(json_file)
                json_df = pd.json_normalize(json_data)

                file_path,file_name=os.path.split(json_file_path)

                # Add a column with the folder path to identify the source
                json_df['folder_path'] = file_path
                json_df['file_name'] = file_name

                # Concatenate with the main DataFrame
                df = pd.concat([df, json_df], ignore_index=True)

        df.fillna('', inplace=True)

        return df

    def convert_dicom_to_nifti(self, dcmfolder):
        """Convert DICOM files into NIfTI files"""

        import os
        import pydicom

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

        try: # convert original DICOM file into NIfTI file
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

    def run_mideface(self, t1w_files_to_deface, dcmfolder, outdir):
        """Perform defacing on the NIfTI T1 files. Mideface algorithm from Freesrufer is
        used for defacing"""

        import os
        import shutil

        fshome = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer"
        subjects_dir = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"
        mideface_path = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer/bin/mideface"

        for file in t1w_files_to_deface:

            # Find full path to the json file
            filename_json =  os.path.join(dcmfolder, file)

            # Find full path to the NIfTI file
            basename = os.path.splitext(file)[0]
            file_path_nii = os.path.join(dcmfolder, f'{basename}.nii')

            outfile_mgz = os.path.join(dcmfolder, f'{basename}.mgz')
            outfile_defaced_mgz = os.path.join(outdir, f'{basename}_defaced.mgz')
            outfile_defaced_nifti = os.path.join(outdir, 'tmpdeface', f'{basename}.nii')
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
                + f" && mri_convert {file_path_nii} {outfile_mgz}" \
                + f" && {mideface_path} --i {outfile_mgz} --o {outfile_defaced_mgz} --odir {qa}" \
                + f" && mri_convert {outfile_defaced_mgz} {outfile_defaced_nifti}"

            self.run_cmd(cmd,"Error DeFaceing image")

            # Copy corresponding json file in the same folder
            destination_path = os.path.join(outdir, 'tmpdeface')

            shutil.copy(filename_json, destination_path)

            print('======= Done defacing MRI data. =======')

    def copy_flair_files(self, flair_files, dcmfolder, outdir):
        """Move FLAIR files into the same folder where deface NIfTI T1 files are stored"""

        import os
        import shutil

        flair_files_to_copy = flair_files['file_name'].tolist()
        destination_path = os.path.join(outdir, 'tmpdeface')
        for flair_file in flair_files_to_copy:
            flair_file_basename = os.path.splitext(flair_file)[0]

            flair_file_path = os.path.join(dcmfolder, flair_file_basename)
            flair_file_path_nii = f'{flair_file_path}.nii'
            flair_file_path_json = f'{flair_file_path}.json'
            shutil.copy(flair_file_path_nii, destination_path)
            shutil.copy(flair_file_path_json, destination_path)

    def deface_mri(self, method: str, path_to_files: str, outdir_path: str) -> None:
        import os
        import pydicom
        import sys
        import shutil

        dcmfolder = path_to_files
        outdir = os.path.join(outdir_path, "defaced")

        # - Create outfolder
        os.makedirs(os.path.join(outdir_path,'defaced/tmpdeface'), exist_ok = True)

        self.convert_dicom_to_nifti(dcmfolder)

        # All nifti files
        all_nii_files = [xx for xx in os.listdir(dcmfolder) if xx.endswith(".nii")]

        # All corresponding json files
        all_json_files = [os.path.join(dcmfolder, xx) for xx in os.listdir(dcmfolder) \
                          if xx.endswith(".json")]

        mri_metadata = self.read_json_files(all_json_files)

        # Extract T1 files
        t1w_files = self.find_T1w(mri_metadata)

        # Extract FLAIR files
        flair_files = self.find_flair(mri_metadata)

        # Extract all files which needs to be defaced
        t1w_files_to_deface = t1w_files['file_name'].tolist()

        # - Deface using Freesurfer
        if method == 'freesurfer':
            if t1w_files_to_deface:
                self.run_mideface(t1w_files_to_deface, dcmfolder, outdir)
            else:
                print("--- T1 is not recognized within uploaded sequences. ---")
                return
        else:
            print(' Wrong defacing method. It has to be ')
            sys.exit()

        # Copy Flair files into same folder where defaced files are
        self.copy_flair_files(flair_files, dcmfolder, outdir)

    def download_file(self, deface_path: str) -> None:
        import boto3
        from botocore.client import Config
        import zipfile
        import os
        import shutil

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
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

    def update_filename_pid_mapping(self, obj_name, personal_id, s3_local):
        import csv
        import io

        folder = "file_pid/"
        filename = "filename_pid.csv"
        file_path = f"{folder}{filename}"

        bucket_local = s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)
        obj_files = bucket_local.objects.filter(Prefix=folder, Delimiter="/")

        if (len(list(obj_files))) > 0:
            existing_object = \
                s3_local.Object(self.__OBJ_STORAGE_BUCKET_LOCAL__, file_path)
            existing_data = existing_object.get()["Body"].read().decode('utf-8')
            data_to_append = [obj_name, personal_id]
            existing_rows = list(csv.reader(io.StringIO(existing_data)))
            existing_rows.append(data_to_append)

            updated_data = io.StringIO()
            csv.writer(updated_data).writerows(existing_rows)
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_fileobj(
                io.BytesIO(updated_data.getvalue().encode('utf-8')), file_path)
        else:
            key_values = ['filename', 'personal_id']
            file_data = [key_values, [obj_name, personal_id]]
            updated_data = io.StringIO()
            csv.writer(updated_data).writerows(file_data)
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_fileobj(
                io.BytesIO(updated_data.getvalue().encode('utf-8')), file_path)

    def upload_file(self, path_to_anonymized_files: str, personal_id: str) -> None:
        import boto3
        from botocore.client import Config
        import os
        import shutil
        from zipfile import ZipFile, ZIP_STORED
        import time
        import logging

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)


        obj_name = os.path.split(path_to_anonymized_files)[1]
        zip_name = os.path.split(path_to_anonymized_files)[0] + "/" + obj_name + \
            "_final.zip"

        # Create zip file with defaced and anonymized data
        files_exists = False
        with ZipFile(zip_name, 'w', ZIP_STORED) as zipObj:
            # Iterate over all the files in directory
            for root, dirs, files in os.walk(path_to_anonymized_files):
                for file in files:
                    if file.endswith('.nii'):
                        files_exists = True
                        # create complete filepath of file in directory
                        file_path = os.path.join(root, file)
                        basename_zip = os.path.basename(path_to_anonymized_files)
                        second_part_of_zip_name = root.split(basename_zip)[1]
                        name_in_zipped_file = basename_zip + \
                            os.path.split(second_part_of_zip_name)[0]
                        name_in_zipped_file = os.path.join(name_in_zipped_file, file)

                        # Add file to zip
                        zipObj.write(file_path, name_in_zipped_file,
                                     compress_type=ZIP_STORED)

                        # Add corresponding json file
                        file_path_json = os.path.splitext(file_path)[0] + ".json"
                        name_in_zipped_file_json = \
                            os.path.splitext(name_in_zipped_file)[0] + ".json"
                        zipObj.write(file_path_json, name_in_zipped_file_json,
                                     compress_type=ZIP_STORED)
                    else:
                        continue

        # Upload output zip file with defaced and anonymized data
        if files_exists:
            ts = round(time.time()*1000)
            folder_name = "MRIs"
            name_of_file_minio = f"{folder_name}/{obj_name}_{ts}.zip"
            try:
                s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)\
                    .upload_file(zip_name,name_of_file_minio)
                print('======= File is uploaded to the local storage. =======')
            except Exception as e:
                logging.error(e)

            # Update key value file with mapping between filename and patient id,
            # this file is stored in the local MinIO instance
            self.update_filename_pid_mapping(name_of_file_minio, personal_id, s3_local)

        # Remove data
        shutil.rmtree(os.path.split(path_to_anonymized_files)[0])

        name_of_file = name_of_file_minio if files_exists else None
        return name_of_file

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

                except: # if some error occurs during deidentification
                    # remove output of current data and just continue with other datasets
                    shutil.rmtree(os.path.join(outdir_path, "defaced"))
                    logging.error("Impossible to deidentify files within " \
                                  f"{basename+current_basename} folder")
                    continue

            else: # if there are no files, just continue on another level,
                # to find directory which have files
                continue

    def generate_personal_id(self, personal_data):
        """Based on the identity, full_name and date of birth."""

        import hashlib

        personal_id = "".join(str(data) for data in personal_data)

        # Remove all whitespaces characters
        personal_id = "".join(personal_id.split())

        # Generate ID
        id = hashlib.sha256(bytes(personal_id, "utf-8")).hexdigest()
        return id

    def create_personal_identifier(self, data_info):
        import pandas as pd
        # Generate personal id
        if all(param is not None for param in [data_info['name'],
                                               data_info['surname'],
                                               data_info['date_of_birth'],
                                               data_info['unique_id']]):

            # Make unified dates, so that different formats of date doesn't change the
            # final id
            data_info["date_of_birth"] = pd.to_datetime(data_info["date_of_birth"],
                                                        dayfirst=True)

            data_info["date_of_birth"] = data_info["date_of_birth"].strftime("%d-%m-%Y")

            # Personal id is made based on name, surname, date date of birth, and national
            # unique id
            personal_data = [data_info["name"], data_info["surname"],
                             data_info["date_of_birth"], data_info["unique_id"]]

            personal_id = self.generate_personal_id(personal_data)
        else:
            # If the data is not provided create an empty string for the personal ID
            personal_data = []
            personal_id = self.generate_personal_id(personal_data)

        return personal_id

    def check_files_in_deideintifed_mri(self, path_zip_file):
        import zipfile

        # Check if the content of uploaded zip file is only consisted of .nii
        # and .json files
        allowed_files = {'.nii', '.json', '.NII', '.JSON'}

        with zipfile.ZipFile(path_zip_file, 'r') as zip_ref:
            # Get the list of all items in the ZIP archive
            for file_name in zip_ref.namelist():
                if not file_name.endswith('/'):
                    if not file_name.endswith(tuple(allowed_files)):
                        return False
        return True

    def upload_already_anonymized_and_defaced_mri(self, path_to_data,
                                                  input_meta):
        """If the uploaded data already anonymized and defaced, check the
        content and directly upload data on local and cloud object storage."""

        import boto3
        from botocore.client import Config
        import os
        import shutil
        import time

        # Download the file which needs to be uploaded
        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=\
                                    self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)

        # Existing non annonymized data in local MinIO bucket
        bucket_local = s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)
        obj_personal_data = bucket_local.objects.filter(Prefix="mri_data/",
                                                        Delimiter="/")

        # Files which needs to be uploaded
        files_to_upload = [obj.key for obj in obj_personal_data]

        # Remove data directories and zip files if exists
        # Before download it is not expected to have data for processing inside
        # this directory
        for item in os.listdir(path_to_data):
            current_item = os.path.join(path_to_data, item)
            if os.path.isdir(current_item):
                shutil.rmtree(current_item)
            if item.endswith(".tmp.part") or item.endswith(".zip"):
                os.remove(current_item)

        # Download data
        file_name = files_to_upload[0]
        basename = os.path.basename(file_name)
        basename_without_ext, _ = \
            os.path.splitext(os.path.splitext(basename)[0])
        path_zip_file = f'{path_to_data}{basename_without_ext}.zip'

        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).download_file(
            file_name, path_zip_file)

        # Delete original file in local storage
        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).objects.filter(
            Prefix=file_name).delete()

        valid_files = self.check_files_in_deideintifed_mri(path_zip_file)

        if valid_files:
            # Create personal id
            personal_id = self.create_personal_identifier(input_meta.data_info)

            # Upload output zip file with defaced and anonymized data
            ts = round(time.time()*1000)
            folder_name = "MRIs"
            name_of_file_minio = \
                f"{folder_name}/{basename_without_ext}_{ts}.zip"
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_file(
                path_zip_file, name_of_file_minio)

            print('======= File is uploaded to the local storage. =======')

            # Update key value file with mapping between filename and patient
            # id, this file is stored in the local MinIO instance
            self.update_filename_pid_mapping(name_of_file_minio, personal_id,
                                             s3_local)

            # Remove data
            os.remove(path_zip_file)

        else:
            name_of_file_minio = None
            os.remove(path_zip_file)
            raise ValueError("Uploaded file contains files other than .nii and .json files")

        return name_of_file_minio

    def action(self, input_meta: PluginExchangeMetadata = None) -> \
        PluginActionResponse:
        """Run defacing algorithm.
        Remove all personal metadata.
        """
        import os
        import logging
        import shutil

        try:
            # Path where original and defaced data will be stored during
            # defacing and anonymisation
            path_to_data = \
                "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"

            name_of_anonymized_files = []

            if input_meta.data_info["upload_anonymized_and_defaced_data"]:
                file_name = \
                    self.upload_already_anonymized_and_defaced_mri(
                        path_to_data, input_meta)
                name_of_anonymized_files.append(file_name)
            else:
                # Download data to process
                self.download_file(path_to_data)
                data_dirs = os.listdir(path_to_data)

                for dir in data_dirs:
                    current_path = os.path.join(path_to_data, dir)

                    if os.path.isdir(current_path):
                        path_to_copied_structure = os.path.join(path_to_data,
                                                                "deidentified",
                                                                dir)
                        self.reproduce_directory_tree(current_path,
                                                      path_to_copied_structure)

                        # Perform defacing and anonymisation of the DICOM files
                        self.deidentify_files(current_path,
                                              path_to_copied_structure)

                        # Create personal id
                        personal_id = self.create_personal_identifier(
                            input_meta.data_info)

                        # Upload processed data
                        name_of_file = self.upload_file(
                            path_to_copied_structure, personal_id)

                        name_of_anonymized_files.append(name_of_file)
                        shutil.rmtree(os.path.join(current_path))

        except Exception as e:
            logging.error(e)

        return PluginActionResponse(None, None, name_of_anonymized_files,
                                    input_meta.data_info)

